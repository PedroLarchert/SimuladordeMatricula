# Dicionário de disciplinas (exemplo para um semestre, você pode completar para todos os semestres)
1
disciplinas = {
    # 1º Semestre
    "MATA02": {"nome": "CÁLCULO A", "pre_requisitos": [], "semestre": 1},
    "MATA37": {"nome": "INTRODUÇÃO À LÓGICA DE PROGRAMAÇÃO", "pre_requisitos": [], "semestre": 1},
    "MATA39": {"nome": "SEMINÁRIOS DE INTRODUÇÃO AO CURSO", "pre_requisitos": [], "semestre": 1},
    "MATA42": {"nome": "MATEMÁTICA DISCRETA I", "pre_requisitos": [], "semestre": 1},
    "MATA68": {"nome": "COMPUTADOR, ÉTICA E SOCIEDADE", "pre_requisitos": [], "semestre": 1},

    # 2º Semestre
    "ADME99": {"nome": "ECONOMIA DA INOVAÇÃO", "pre_requisitos": [], "semestre": 2},
    "MATC73": {"nome": "INTRODUÇÃO À LÓGICA MATEMÁTICA", "pre_requisitos": ["MATA42"], "semestre": 2},
    "MATC90": {"nome": "CIRCUITOS DIGITAIS E ARQUITETURA DE COMPUTADORES", "pre_requisitos": [], "semestre": 2},
    "MATC92": {"nome": "FUNDAMENTOS DE SISTEMAS DE INFORMAÇÃO", "pre_requisitos": [], "semestre": 2},
    "MATD04": {"nome": "ESTRUTURAS DE DADOS", "pre_requisitos": ["MATA37", "MATA42"], "semestre": 2},

    # 3º Semestre
    "ADM001": {"nome": "INTRODUÇÃO À ADMINISTRAÇÃO", "pre_requisitos": [], "semestre": 3},
    "MATA07": {"nome": "ÁLGEBRA LINEAR", "pre_requisitos": [], "semestre": 3},
    "MATA55": {"nome": "PROGRAMAÇÃO ORIENTADA A OBJETOS", "pre_requisitos": ["MATD04"], "semestre": 3},
    "MATA58": {"nome": "SISTEMAS OPERACIONAIS", "pre_requisitos": ["MATC90"], "semestre": 3},
    "MATC94": {"nome": "INTRODUÇÃO ÀS LINGUAGENS FORMAIS E TEORIA DA COMPUTAÇÃO", "pre_requisitos": ["MATA42"], "semestre": 3},

    # 4º Semestre
    "LETA09": {"nome": "OFICINA DE LEITURA E PRODUÇÃO DE TEXTOS", "pre_requisitos": [], "semestre": 4},
    "MAT236": {"nome": "MÉTODOS ESTATÍSTICOS", "pre_requisitos": ["MATA02", "MATA07"], "semestre": 4},
    "MATA59": {"nome": "REDES DE COMPUTADORES I", "pre_requisitos": ["MATC90"], "semestre": 4},
    "MATA62": {"nome": "ENGENHARIA DE SOFTWARE I", "pre_requisitos": ["MATA55"], "semestre": 4},
    "MATC82": {"nome": "SISTEMAS WEB", "pre_requisitos": ["MATA58", "MATC92"], "semestre": 4},

    # 5º Semestre
    "ADM211": {"nome": "MÉTODOS QUANTITATIVOS APLICADOS À ADMINISTRAÇÃO", "pre_requisitos": ["ADM001", "MAT236"], "semestre": 5},
    "MATA56": {"nome": "PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO", "pre_requisitos": ["MATA55", "MATD04"], "semestre": 5},
    "MATA60": {"nome": "BANCO DE DADOS", "pre_requisitos": ["MATD04"], "semestre": 5},
    "MATA63": {"nome": "ENGENHARIA DE SOFTWARE II", "pre_requisitos": ["MATA62"], "semestre": 5},
    "MATC84": {"nome": "LABORATÓRIO DE PROGRAMAÇÃO WEB", "pre_requisitos": ["MATA55"], "semestre": 5},

    # 6º Semestre
    "ADMF01": {"nome": "SISTEMAS DE APOIO À DECISÃO", "pre_requisitos": ["ADM211"], "semestre": 6},
    "MAT220": {"nome": "EMPREENDEDORES EM INFORMÁTICA", "pre_requisitos": [], "semestre": 6},
    "MATA79": {"nome": "LINGUAGENS PARA APLICAÇÃO COMERCIAL", "pre_requisitos": ["MATA37"], "semestre": 6},
    "MATB09": {"nome": "LABORATÓRIO DE BANCO DE DADOS", "pre_requisitos": ["MATA60"], "semestre": 6},
    "MATC89": {"nome": "APLICAÇÕES PARA DISPOSITIVOS MÓVEIS", "pre_requisitos": ["MATA55", "MATA59"], "semestre": 6},

    # 7º Semestre
    "MATA64": {"nome": "INTELIGÊNCIA ARTIFICIAL", "pre_requisitos": ["MATC73", "MATD04"], "semestre": 7},
    "MATB02": {"nome": "QUALIDADE DE SOFTWARE", "pre_requisitos": ["MATA63"], "semestre": 7},
    "MATB19": {"nome": "SISTEMAS MULTIMÍDIA", "pre_requisitos": ["MATA55"], "semestre": 7},
    "MATC72": {"nome": "INTERAÇÃO HUMANO-COMPUTADOR", "pre_requisitos": ["MATA62"], "semestre": 7},
    "MATC99": {"nome": "SEGURANÇA E AUDITORIA DE SISTEMAS DE INFORMAÇÃO", "pre_requisitos": ["ADMIF01", "MATA07"], "semestre": 7},

    # 9º Semestre
    "MATC97": {"nome": "TCC BACHARELADO SISTEMAS DE INFORMAÇÃO I", "pre_requisitos": ["LETA09"], "semestre": 9},
    # 10º Semestre
    "MATC 98": {"nome": "TCC BACHARELADO SISTEMAS DE INFORMAÇÃO II", "pre_requisitos": ["MATC97"], "semestre": 10},
}


# Função para verificar se os pré-requisitos de uma disciplina foram atendidos
def prerequisitos_atingidos(materias_concluidas, disciplina):
    return all(pre in materias_concluidas for pre in disciplina["pre_requisitos"])

# Função para mostrar disciplinas disponíveis no semestre


def disciplinas_disponiveis(semestre_atual, materias_concluidas):
    # Disciplinas de semestres anteriores não concluídas
    anteriores = [codigo for codigo, disciplina in disciplinas.items()
                  if disciplina["semestre"] < semestre_atual and codigo not in materias_concluidas]

    # Disciplinas do semestre atual
    atuais = [codigo for codigo, disciplina in disciplinas.items()
              if disciplina["semestre"] == semestre_atual and prerequisitos_atingidos(materias_concluidas, disciplina) and codigo not in materias_concluidas]

    # Disciplinas de semestres posteriores com pré-requisitos atingidos
    posteriores = [codigo for codigo, disciplina in disciplinas.items()
                   if disciplina["semestre"] > semestre_atual and prerequisitos_atingidos(materias_concluidas, disciplina) and codigo not in materias_concluidas]

    return anteriores + atuais + posteriores

# Função para verificar se todas as disciplinas foram concluídas


def todas_disciplinas_concluidas(materias_concluidas):
    return set(materias_concluidas) == set(disciplinas.keys())

# Função principal para simular a matrícula


def simular_matricula():
    semestre_atual = 1
    materias_concluidas = []

    while semestre_atual <= 10:
        if todas_disciplinas_concluidas(materias_concluidas):
            print("\nParabéns! Você concluiu todas as disciplinas e está formado!")
            return

        print(f"\nSemestre {semestre_atual}")
        materias_disponiveis = disciplinas_disponiveis(
            semestre_atual, materias_concluidas)

        if not materias_disponiveis:
            print("Nenhuma disciplina disponível para esse semestre.")
            break

        print("Disciplinas disponíveis:")
        for i, materia in enumerate(materias_disponiveis):
            print(f"{i+1}. {disciplinas[materia]['nome']} (Código: {materia})")

        while True:
            escolhas = input(
                "Escolha as disciplinas (números separados por vírgula) ou 's' para sair: ").strip()
            if escolhas.lower() == 's':
                print("Matrícula encerrada.")
                return

            try:
                escolhas_indices = [int(x.strip())
                                    for x in escolhas.split(",") if x.strip()]
                if all(1 <= indice <= len(materias_disponiveis) for indice in escolhas_indices):
                    break
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print(
                    "Entrada inválida. Por favor, insira números separados por vírgula.")

        for indice in escolhas_indices:
            materia_escolhida = materias_disponiveis[indice - 1]
            materias_concluidas.append(materia_escolhida)
            print(f"Disciplina '{
                  disciplinas[materia_escolhida]['nome']}' adicionada com sucesso.")

        semestre_atual += 1

    print("\nMatrícula finalizada. Disciplinas concluídas:")
    for materia in materias_concluidas:
        print(f"{disciplinas[materia]['nome']} (Código: {materia})")


# Executar o programa
simular_matricula()
