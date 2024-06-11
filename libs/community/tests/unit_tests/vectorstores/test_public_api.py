"""Test the public API of the tools package."""
from langchain_community.vectorstores import __all__ as public_api

_EXPECTED = [
    "AlibabaCloudOpenSearch",
    "AlibabaCloudOpenSearchSettings",
    "AnalyticDB",
    "Annoy",
    "ApacheDoris",
    "AtlasDB",
    "AwaDB",
    "AzureSearch",
    "Bagel",
    "BaiduVectorDB",
    "BESVectorStore",
    "BigQueryVectorSearch",
    "Cassandra",
    "AstraDB",
    "Chroma",
    "Clarifai",
    "Clickhouse",
    "ClickhouseSettings",
    "DashVector",
    "DatabricksVectorSearch",
    "DeepLake",
    "Dingo",
    "DistanceStrategy",
    "DocArrayHnswSearch",
    "DocArrayInMemorySearch",
    "DocumentDBVectorSearch",
    "DuckDB",
    "EcloudESVectorStore",
    "ElasticKnnSearch",
    "ElasticVectorSearch",
    "ElasticsearchStore",
    "Epsilla",
    "FAISS",
    "HanaDB",
    "Hologres",
    "InfinispanVS",
    "InMemoryVectorStore",
    "KDBAI",
    "Kinetica",
    "KineticaSettings",
    "LanceDB",
    "Lantern",
    "LLMRails",
    "Marqo",
    "MatchingEngine",
    "Meilisearch",
    "Milvus",
    "MomentoVectorIndex",
    "MongoDBAtlasVectorSearch",
    "MyScale",
    "MyScaleSettings",
    "Neo4jVector",
    "OpenSearchVectorSearch",
    "OracleVS",
    "PGEmbedding",
    "PGVector",
    "PathwayVectorClient",
    "Pinecone",
    "Qdrant",
    "Redis",
    "Relyt",
    "Rockset",
    "SKLearnVectorStore",
    "ScaNN",
    "SemaDB",
    "SingleStoreDB",
    "SQLiteVSS",
    "StarRocks",
    "SupabaseVectorStore",
    "SurrealDBStore",
    "Tair",
    "TiDBVectorStore",
    "TileDB",
    "Tigris",
    "TimescaleVector",
    "Typesense",
    "UpstashVectorStore",
    "USearch",
    "Vald",
    "VDMS",
    "Vearch",
    "Vectara",
    "VespaStore",
    "VLite",
    "Weaviate",
    "ZepVectorStore",
    "Zilliz",
    "TencentVectorDB",
    "AzureCosmosDBVectorSearch",
    "VectorStore",
    "Yellowbrick",
    "NeuralDBVectorStore",
    "CouchbaseVectorStore",
]


def test_public_api() -> None:
    """Test for regressions or changes in the public API."""
    # Check that the public API is as expected
    assert set(public_api) == set(_EXPECTED)