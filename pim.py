usuario_professor = {}
usuario_aluno = {}
turmas = {}
atividades = {}  

tela = "menu_identificação"

while tela != "sair":
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

    elif tela == "login_professo":
        professor_login = int(input("\n1-Fazer Login\n2-Criar Conta\n0-Voltar\n"))
        if professor_login == 0:
            tela = "menu_identificação"
        elif professor_login == 1:
            print("[LOGIN PROFESSOR]\n(0-voltar)")
            while True:
                User = input("Usuário: ")
                senha = input("Senha: ")
                if User == "0":
                    tela = "login_professo"
                    break
                if User in usuario_professor and usuario_professor[User] == senha:
                    tela = "menu_professor"
                    break
                else:
                    print("Senha ou Usuario Invalido")
        elif professor_login == 2:
            print("[CRIAR CONTA]\n")
            ID = input("Insira seu Usuario: ")
            Senha = input("Insira sua Senha: ")
            usuario_professor[ID] = Senha
            tela = "login_professo"

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

    elif tela == "menu_atividades":
        print("\n[MARCAR ATIVIDADES/PROVAS]\n")

        if len(turmas) == 0:
            print("Nenhuma turma cadastrada ainda.\n")
            input("Pressione ENTER para voltar")
            tela = "menu_professor"
            continue

        print("Turmas disponíveis:\n")
        for i, turma in enumerate(turmas.keys(), start=1):
            print(f"{i} - Turma {turma}")

        escolha_turma = input("\nDigite o número da turma ou 0 para voltar: ")

        if escolha_turma == "0":
            tela = "menu_professor"
            continue

        try:
            escolha_turma = int(escolha_turma)
            turma_escolhida = list(turmas.keys())[escolha_turma - 1]
        except (ValueError, IndexError):
            print("Opção inválida!\n")
            tela = "menu_professor"
            continue

        materia = input("Digite o nome da matéria: ")
        evento = input("Digite o nome do evento (ex: Prova 3º bimestre, Entrega de atividade avaliativa): ")

        data = input("Digite a data do evento (formato DD/MM/AAAA): ")
            

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

    elif tela == "login_aluno":
        print("[LOGIN ALUNO]\n(0-Voltar)")
        while True:
            matricula = input("Matricula: ")
            senha = input("Senha: ")
            if matricula == "0":
                tela = "menu_identificação"
                break
            if matricula in usuario_aluno and usuario_aluno[matricula]["senha"] == senha:
                tela = "menu_aluno"
                break
            else:
                print("Senha ou Usuario Invalido")

    elif tela == "menu_aluno":
        print("[ALUNO]\n")
        mn_aluno = int(input("1-Notas\n2-Provas/Atividades\n3-Horarios de Alulas\n0-Voltar\n"))
        if mn_aluno == 0:
            tela = "login_aluno"
        elif mn_aluno == 1:
            print("\n[SUAS NOTAS]\n")
            for materia, nota in usuario_aluno[matricula].get("notas", {}).items():
                print(f"{materia}: {nota}")
            input("\nPressione ENTER para voltar")
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

    elif tela == "Aluno_Professor":
        print("[GERENCIAMENTO DE ALUNOS]\n")
        aluno_prof = int(input("1-Administrar Alunos\n2-Cadastrar Aluno\n0-Voltar\n"))
        if aluno_prof == 0:
            tela = "menu_professor"
        elif aluno_prof == 1:
            tela = "Administrar_Alunos"
        elif aluno_prof == 2:
            tela = "Cadastro_Aluno"

    elif tela == "Cadastro_Aluno":
        print("[CADASTRAR ALUNO]\n")
        matricula = input("Matricula: ")

        if matricula in usuario_aluno:
            print("\nMatrícula já cadastrada! Tente outra.\n")
            tela = "Aluno_Professor"
            continue

        nome = input("Nome: ")
        turma = input("Turma: ")
        senha_aluno = input("Senha: ")

        usuario_aluno[matricula] = {
            "nome": nome,
            "turma": turma,
            "senha": senha_aluno,
            "notas": {}
        }

        if turma not in turmas:
            turmas[turma] = []
        turmas[turma].append(matricula)

        print("\nALUNO CADASTRADO COM SUCESSO!\n")
        tela = "Aluno_Professor"

    elif tela == "Administrar_Alunos":
        print("\n[LISTA DE ALUNOS CADASTRADOS]\n")

        if len(usuario_aluno) == 0:
            print("Nenhum aluno cadastrado ainda.\n")
        else:
            for matricula, dados in usuario_aluno.items():
                print(f"Nome: {dados['nome']} | Turma: {dados['turma']}")

        input("\nPressione ENTER para voltar")
        tela = "Aluno_Professor"

    elif tela == "menu_notas":
        print("\n[MENU DE NOTAS - PROFESSOR]\n")

        if len(usuario_aluno) == 0:
            print("Nenhum aluno cadastrado!\n")
            input("Pressione ENTER para voltar")
            tela = "menu_professor"
            continue

        print("Alunos disponíveis:\n")
        for i, (matricula, dados) in enumerate(usuario_aluno.items(), start=1):
            print(f"{i} - {dados['nome']} - Turma: {dados['turma']}")

        escolha = input("\nDigite o número do aluno ou 0 para voltar: ")

        if escolha == "0":
            tela = "menu_professor"
            continue

        try:
            escolha = int(escolha)
            matricula_selecionada = list(usuario_aluno.keys())[escolha - 1]
        except (ValueError, IndexError):
            print("Opção inválida!")
            tela = "menu_professor"
            continue

        materia = input("Digite a matéria: ")
        nota = float(input("Digite a nota (0 a 10): "))

        usuario_aluno[matricula_selecionada]["notas"][materia] = nota

        print(f"\nNota registrada para {usuario_aluno[matricula_selecionada]['nome']} em {materia}: {nota}\n")
        input("Pressione ENTER para voltar")
        tela = "menu_professor"
