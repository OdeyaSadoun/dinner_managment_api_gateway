class Serializer:
    @staticmethod
    def serialize_data(data):
        if hasattr(data, "to_dict"):
            return data.to_dict()
        elif hasattr(data, "dict"):
            return data.dict()
        elif isinstance(data, dict):
            return {key: Serializer.serialize_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [Serializer.serialize_data(item) for item in data]
        else:
            return data
