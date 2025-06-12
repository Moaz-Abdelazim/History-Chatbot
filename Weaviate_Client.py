import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import pandas as pd

@dataclass
class WeaviateConfig:
    url: str
    api_key: str
    collection_name: str = "HistoricalChatbot"

class WeaviateClient:
    def __init__(self, config: WeaviateConfig):
        self.config = config
        self.client = None
        self.collection = None

    def connect(self) -> None:
        """Establish connection to Weaviate"""
        try:
            self.client = weaviate.connect_to_weaviate_cloud(
                cluster_url=self.config.url,
                auth_credentials=Auth.api_key(self.config.api_key),
            )
            print(f"Connection status: {self.client.is_ready()}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Weaviate: {str(e)}")

    def create_collection(self) -> None:
        """Create a new collection with specified configuration"""
        try:
            self.client.collections.create(
                name=self.config.collection_name,
                properties=[
                    Property(name="text", data_type=DataType.TEXT),
                ],
                vectorizer_config=[
                    Configure.NamedVectors.text2vec_weaviate(
                        name="chatbot",
                        source_properties=["text"],
                        model="Snowflake/snowflake-arctic-embed-l-v2.0",
                    )
                ]
            )
            self.collection = self.client.collections.get(self.config.collection_name)
        except Exception as e:
            raise RuntimeError(f"Failed to create collection: {str(e)}")

    def get_collection(self) -> Any:
        try:
            self.collection = self.client.collections.get(self.config.collection_name)
            return self.collection
        except Exception as e:
            raise RuntimeError(f"Failed to get collection: {str(e)}")

    def batch_import_data(self, texts: List[str], batch_size: int = 200) -> None:
        """Import data in batches from a list of texts"""
        with self.collection.batch.fixed_size(batch_size=batch_size) as batch:
            for text in texts:
                batch.add_object(
                    properties={"text": text}
                )
                if batch.number_errors > 10:
                    print("Batch import stopped due to excessive errors.")
                    break

        failed_objects = self.collection.batch.failed_objects
        if failed_objects:
            print(f"Number of failed imports: {len(failed_objects)}")
            print(f"First failed object: {failed_objects[0]}")

    def search(self, query: str, limit: int = 5, properties: List[str] = None) -> List[Dict[str, Any]]:
        if not self.collection:
            raise RuntimeError("Collection not initialized")
        try:
            if properties is None:
                properties = ["text"]

            response = self.collection.query.near_text(
                query=query,
                limit=limit,
                return_properties=properties
            )
            sorted_results = sorted(response.objects, key=lambda obj: getattr(obj, 'score', 0), reverse=True)
            concatenated_text = ", ".join([obj.properties['text'] for obj in sorted_results if 'text' in obj.properties])
 

            return concatenated_text

        except Exception as e:
            raise RuntimeError(f"Search failed: {str(e)}")

    def close(self) -> None:
        """Close the Weaviate client connection"""
        if self.client:
            self.client.close()

def load_historical_data(filepath: str,weaviate_client: WeaviateClient) -> List[Dict[str, Any]]:
    """Load and format historical data from CSV file"""
    try:
        df = pd.read_csv(filepath)
     
        print(len(df))
        historical_data=df['Text'].to_list()
        print(len(df))
        weaviate_client.batch_import_data(historical_data)            

        return historical_data
    except Exception as e:
        print(f"Error loading historical data: {str(e)}")
        return []

def searchForSimiliratiy(query: str, limit: int = 5):
    config = WeaviateConfig(
        url='ejz2hh2hqj2d7kgs7fi6hg.c0.us-east1.gcp.weaviate.cloud',
        api_key='NSS3LVsnzgsbzy1JxtcsOUWqEsF0FuSGxw2D')
    
    weaviate_client = WeaviateClient(config)
    try:
        weaviate_client.connect()
        # weaviate_client.create_collection()
        weaviate_client.get_collection()
        # load_historical_data('data/history_dataset.csv',weaviate_client)
        print("\nSearching for historical events:")
        context = weaviate_client.search(
            query=query,
            limit=limit)
    finally:
        weaviate_client.close()
    return context    

# context =searchForSimiliratiy(query="The Great Pyramid of Giza and its historical significance", limit=5)

