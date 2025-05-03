'''
SINGLE RESPONSABILITY PRINCIPLE

Solução refatorada seguindo o Princípio da Responsabilidade Única.
Cada classe tem uma única responsabilidade bem definida.
'''

class APIConnector:
    def connect_api(self):
        # Lógica para conectar à API
        pass

class TaskManager:
    def __init__(self, api_connector):
        self.api_connector = api_connector

    def create_task(self):
        # Lógica para criar tarefa
        pass

    def update_task(self):
        # Lógica para atualizar tarefa
        pass

    def remove_task(self):
        # Lógica para remover tarefa
        pass

class NotificationService:
    def send_notification(self):
        # Lógica para enviar notificação
        pass

class ReportGenerator:
    def generate_report(self):
        # Lógica para gerar relatório
        pass

class ReportSender:
    def send_report(self):
        # Lógica para enviar relatório
        pass

# Exemplo de uso:
api_connector = APIConnector()
task_manager = TaskManager(api_connector)
notification_service = NotificationService()
report_generator = ReportGenerator()
report_sender = ReportSender()

