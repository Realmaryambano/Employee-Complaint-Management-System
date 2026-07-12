import oracledb


def get_connection():

    connection = oracledb.connect(
        user="ECMS",
        password="Marya@123",
        host="localhost",
        port=1521,
        service_name="free"
    )

    return connection