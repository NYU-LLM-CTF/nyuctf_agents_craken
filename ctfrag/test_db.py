from pymilvus import connections, utility

connections.connect(
    alias="default",
    host="0.0.0.0",
    port="19530"
)

if connections.has_connection("default"):
    print("Connected to Milvus.")

collections = utility.list_collections()
print("Current Collections:", collections)

connections.disconnect("default")