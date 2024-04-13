from abc import abstractmethod


class Base:
    @abstractmethod
    def create_table(create_query=None):
        raise NotImplementedError("Define abstractmethod 'create_table'")

    @abstractmethod
    def insert_data(self):
        raise NotImplementedError("Define abstractmethod 'input_data'")

    @abstractmethod
    def delete_data(self, id_delete):
        raise NotImplementedError("Define abstractmethod 'delete_data'")

    @abstractmethod
    def find_info(self):
        raise NotImplementedError("Define abstractmethod 'find_info'")

    @abstractmethod
    def update_data(self):
        raise NotImplementedError("Define abstractmethod 'update_data'")
