# ============================================================
#  SISTEMA DE GESTÃO ESCOLAR - PROJETO PIM (ADS - 1º PERÍODO)
# ============================================================

# DICIONÁRIOS PRINCIPAIS -------------------------------------
usuario_professor = {}  # Armazena usuário e senha dos professores
usuario_aluno = {}      # Armazena matrícula, nome, senha, turma e notas dos alunos
turmas = {}             # Armazena as turmas e suas matrículas correspondentes
atividades = {}         # Armazena atividades e provas (matéria, nome do evento e data)
# ------------------------------------------------------------


# VARIÁVEL DE CONTROLE DE TELA -------------------------------
# Todo o sistema roda dentro de um "while", e a variável "tela"
# define qual parte do programa está sendo exibida no momento.
tela = "menu_identificação"
# ------------------------------------------------------------


# LOOP PRINCIPAL DO SISTEMA ----------------------------------
while tela != "sair":

    # ========================================================
    # MENU DE IDENTIFICAÇÃO
    # ========================================================
    if tela == "menu_identificação":
        print("\n[MENU DE IDENTIFICAÇÃO]")
        print("Escolha:\n")
        mn_Identificação = int(input("1-Professor\n2-Aluno\n0-Sair\n"))

        if mn_Identificação == 1:
            tela = "login_professo"
        elif mn_Identificação == 2:
            tela = "login_aluno"
        elif mn_Identificação == 0:
            tela = "sair"

    # ========================================================
    # LOGIN / CADASTRO DE PROFESSOR
    # ========================================================
    elif tela == "login_professo":
        professor_login = int(input("\n1-Fazer Login\n2-Criar Conta\n0-Voltar\n"))

        # Retorna ao menu inicial
        if professor_login == 0:
            tela = "menu_identificação"

        # LOGIN DE PROFESSOR EXISTENTE ------------------------
        elif professor_login == 1:
            print("[LOGIN PROFESSOR]\n(0-voltar)")
            while True:
                User = input("Usuário: ")
                senha = input("Senha: ")
                if User == "0":
                    tela = "login_professo"
                    break
                # Verifica se o usuário e senha estão corretos
                if User in usuario_professor and usuario_professor[User] == senha:
                    tela = "menu_professor"
                    break
                else:
                    print("Senha ou Usuário inválido.")

        # CRIAÇÃO DE CONTA DE PROFESSOR -----------------------
        elif professor_login == 2:
            print("[CRIAR CONTA]\n")
            ID = input("Insira seu Usuário: ")
            Senha = input("Insira sua Senha: ")
            usuario_professor[ID] = Senha
            print("\nConta criada com sucesso!\n")
            tela = "login_professo"

    # ========================================================
    # MENU PRINCIPAL DO PROFESSOR
    # ========================================================
    elif tela == "menu_professor":
        print("[MENU PROFESSOR]")
        mn_professor = int(input("1-Alunos\n2-Notas\n3-Marcar Atividades/Provas\n0-Voltar\n"))

        if mn_professor == 0:
            tela = "login_professo"
        elif mn_professor == 1:
            tela = "Aluno_Professor"
        elif mn_professor == 2:
            tela = "menu_notas"
        elif mn_professor == 3:
            tela = "menu_atividades"
        else:
            break

    # ========================================================
    # MENU DE ATIVIDADES E PROVAS (PROFESSOR)
    # ========================================================
    elif tela == "menu_atividades":
        print("\n[MARCAR ATIVIDADES/PROVAS]\n")

        # Verifica se existem turmas cadastradas
        if len(turmas) == 0:
            print("Nenhuma turma cadastrada ainda.\n")
            input("Pressione ENTER para voltar")
            tela = "menu_professor"
            continue

        # Lista todas as turmas
        print("Turmas disponíveis:\n")
        for i, turma in enumerate(turmas.keys(), start=1):
            print(f"{i} - Turma {turma}")

        escolha_turma = input("\nDigite o número da turma ou 0 para voltar: ")

        if escolha_turma == "0":
            tela = "menu_professor"
            continue

        # Verifica se a escolha é válida
        try:
            escolha_turma = int(escolha_turma)
            turma_escolhida = list(turmas.keys())[escolha_turma - 1]
        except (ValueError, IndexError):
            print("Opção inválida!\n")
            tela = "menu_professor"
            continue

        # Coleta os dados da atividade
        materia = input("Digite o nome da matéria: ")
        evento = input("Digite o nome do evento (ex: Prova 3º bimestre): ")
        data = input("Digite a data do evento (formato DD/MM/AAAA): ")  # Campo obrigatório

        # Armazena o evento
        if turma_escolhida not in atividades:
            atividades[turma_escolhida] = []

        atividades[turma_escolhida].append({
            "materia": materia,
            "evento": evento,
            "data": data
        })

        print(f"\nAtividade '{evento}' cadastrada com sucesso para a turma {turma_escolhida}!\n")
        input("Pressione ENTER para voltar")
        tela = "menu_professor"

    # ========================================================
    # LOGIN DO ALUNO
    # ========================================================
    elif tela == "login_aluno":
        print("[LOGIN ALUNO]\n(0-Voltar)")
        while True:
            matricula = input("Matrícula: ")
            senha = input("Senha: ")
            if matricula == "0":
                tela = "menu_identificação"
                break
            # Verifica se matrícula e senha estão corretas
            if matricula in usuario_aluno and usuario_aluno[matricula]["senha"] == senha:
                tela = "menu_aluno"
                break
            else:
                print("Senha ou Usuário inválido.")

    # ========================================================
    # MENU DO ALUNO
    # ========================================================
    elif tela == "menu_aluno":
        print("[ALUNO]\n")
        mn_aluno = int(input("1-Notas\n2-Provas/Atividades\n0-Voltar\n"))

        # Voltar ao login
        if mn_aluno == 0:
            tela = "login_aluno"

        # Ver notas registradas
        elif mn_aluno == 1:
            print("\n[SUAS NOTAS]\n")
            for materia, nota in usuario_aluno[matricula].get("notas", {}).items():
                print(f"{materia}: {nota}")
            input("\nPressione ENTER para voltar")

        # Ver atividades agendadas da turma
        elif mn_aluno == 2:
            turma_aluno = usuario_aluno[matricula]["turma"]
            print(f"\n[ATIVIDADES DA TURMA {turma_aluno}]\n")
            if turma_aluno in atividades:
                for a in atividades[turma_aluno]:
                    print(f"{a['materia']}: {a['evento']} - Data: {a['data']}")
            else:
                print("Nenhuma atividade marcada para sua turma.")
            input("\nPressione ENTER para voltar")

        else:
            break

    # ========================================================
    # GERENCIAMENTO DE ALUNOS (PROFESSOR)
    # ========================================================
    elif tela == "Aluno_Professor":
        print("[GERENCIAMENTO DE ALUNOS]\n")
        aluno_prof = int(input("1-Administrar Alunos\n2-Cadastrar Aluno\n0-Voltar\n"))

        if aluno_prof == 0:
            tela = "menu_professor"
        elif aluno_prof == 1:
            tela = "Administrar_Alunos"
        elif aluno_prof == 2:
            tela = "Cadastro_Aluno"

    # ========================================================
    # CADASTRO DE NOVO ALUNO
    # ========================================================
    elif tela == "Cadastro_Aluno":
        print("[CADASTRAR ALUNO]\n")
        matricula = input("Matrícula: ")

        # Verifica se matrícula já existe
        if matricula in usuario_aluno:
            print("\nMatrícula já cadastrada! Tente outra.\n")
            tela = "Aluno_Professor"
            continue

        nome = input("Nome: ")
        turma = input("Turma: ")
        senha_aluno = input("Senha: ")

        # Cria o registro do aluno
        usuario_aluno[matricula] = {
            "nome": nome,
            "turma": turma,
            "senha": senha_aluno,
            "notas": {}
        }

        # Adiciona o aluno na turma
        if turma not in turmas:
            turmas[turma] = []
        turmas[turma].append(matricula)

        print("\nALUNO CADASTRADO COM SUCESSO!\n")
        tela = "Aluno_Professor"

    # ========================================================
    # CONSULTA DE ALUNOS CADASTRADOS
    # ========================================================
    elif tela == "Administrar_Alunos":
        print("\n[LISTA DE ALUNOS CADASTRADOS]\n")

        if len(usuario_aluno) == 0:
            print("Nenhum aluno cadastrado ainda.\n")
        else:
            for matricula, dados in usuario_aluno.items():
                print(f"Nome: {dados['nome']} | Turma: {dados['turma']}")

        input("\nPressione ENTER para voltar")
        tela = "Aluno_Professor"

    # ========================================================
    # REGISTRO DE NOTAS (PROFESSOR)
    # ========================================================
    elif tela == "menu_notas":
        print("\n[MENU DE NOTAS - PROFESSOR]\n")

        if len(usuario_aluno) == 0:
            print("Nenhum aluno cadastrado!\n")
            input("Pressione ENTER para voltar")
            tela = "menu_professor"
            continue

        # Lista alunos disponíveis
        print("Alunos disponíveis:\n")
        for i, (matricula, dados) in enumerate(usuario_aluno.items(), start=1):
            print(f"{i} - {dados['nome']} - Turma: {dados['turma']}")

        escolha = input("\nDigite o número do aluno ou 0 para voltar: ")

        if escolha == "0":
            tela = "menu_professor"
            continue

        # Seleciona o aluno conforme a escolha do professor
        try:
            escolha = int(escolha)
            matricula_selecionada = list(usuario_aluno.keys())[escolha - 1]
        except (ValueError, IndexError):
            print("Opção inválida!")
            tela = "menu_professor"
            continue

        # Inserção da nota
        materia = input("Digite a matéria: ")
        nota = float(input("Digite a nota (0 a 10): "))

        usuario_aluno[matricula_selecionada]["notas"][materia] = nota

        print(f"\nNota registrada para {usuario_aluno[matricula_selecionada]['nome']} em {materia}: {nota}\n")
        input("Pressione ENTER para voltar")
        tela = "menu_professor"
