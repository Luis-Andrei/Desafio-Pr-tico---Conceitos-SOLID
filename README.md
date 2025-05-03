# Desafio SOLID - Princípios SRP e OCP

Este projeto demonstra a implementação de dois princípios SOLID:
- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)

## Estrutura do Projeto

```
py-desafio-modulo-7-template/
├── 1_S_SRP/
│   └── srp_bad_example.py      # Implementação do SRP
└── 2_O_OCP/
    └── ocp_bad_example.py      # Implementação do OCP
```

## Single Responsibility Principle (SRP)

### Implementação

O SRP foi aplicado dividindo uma classe monolítica `TaskHandler` em classes menores, cada uma com uma única responsabilidade:

- `APIConnector`: Gerencia conexões com a API
- `TaskManager`: Gerencia operações de tarefas (criar, atualizar, remover)
- `NotificationService`: Responsável por enviar notificações
- `ReportGenerator`: Gera relatórios
- `ReportSender`: Envia relatórios

### Benefícios
- Código mais organizado e manutenível
- Facilidade para testar cada componente isoladamente
- Melhor reutilização de código
- Redução de acoplamento entre funcionalidades

## Open/Closed Principle (OCP)

### Implementação

O OCP foi aplicado na gestão de exames médicos, permitindo a adição de novos tipos de exame sem modificar o código existente:

- `Exame` (Interface abstrata): Define o contrato para todos os tipos de exame
- `ExameSangue`: Implementação específica para exames de sangue
- `ExameRaioX`: Implementação específica para exames de raio-x
- `AprovaExame`: Classe que processa a aprovação de qualquer tipo de exame

### Benefícios
- Facilidade para adicionar novos tipos de exame
- Código mais flexível e extensível
- Redução do risco de bugs ao adicionar novas funcionalidades
- Manutenção mais segura do código existente

## Como Usar

### SRP Example
```python
# Criando instâncias
api_connector = APIConnector()
task_manager = TaskManager(api_connector)
notification_service = NotificationService()
report_generator = ReportGenerator()
report_sender = ReportSender()

# Usando os serviços
task_manager.create_task()
notification_service.send_notification()
```

### OCP Example
```python
# Criando instâncias de exames
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

# Aprovando exames
aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
```

## Extensibilidade

### Adicionando Novo Tipo de Exame
Para adicionar um novo tipo de exame, basta criar uma nova classe que herde de `Exame`:

```python
class ExameUltrassom(Exame):
    def __init__(self):
        self.tipo = "ultrassom"

    def verificar_condicoes(self):
        # Implementação específica para ultrassom
        return True
```

## Requisitos
- Python 3.6+
