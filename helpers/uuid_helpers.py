import uuid


class UuidHelpers:

    @staticmethod
    def generate_uuid() -> str:
        uid = uuid.uuid4()
        uid_str = str(uid)
        return uid_str

