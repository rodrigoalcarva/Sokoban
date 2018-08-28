from search import *


class Estado_sokoban:
    def __init__(self,arrumador = (3, 3), caixas = ((2, 2), ), paredes = ((0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2), (4,3), (4,4), (1,4), (2,4), (3,4)), alvos = ((1, 1), )):
        self.arrumador = arrumador
        self.caixas = caixas
        self.paredes = paredes
        self.alvos = alvos

    def arrumador_esquerda(self):
        arrumador_final = (self.arrumador[0], self.arrumador[1] - 1)

        if arrumador_final in self.paredes: #se arrumador contra parede
            return False

        for caixa in self.caixas:
            if caixa == arrumador_final:
                if (caixa[0], caixa[1] - 1) in self.paredes: #se caixa contra parede
                    return False

                if len(self.caixas) > 1:
                    other_boxes = [el for el in self.caixas if el != caixa]

                    if (caixa[0], caixa[1] - 1) in other_boxes: #se caixa contra caixa
                        return False

        return True

    def arrumador_direita(self):
        arrumador_final = (self.arrumador[0], self.arrumador[1] + 1)

        if arrumador_final in self.paredes:
            return False

        for caixa in self.caixas:
            if caixa == arrumador_final:
                if (caixa[0], caixa[1] + 1) in self.paredes:
                    return False

                if len(self.caixas) > 1:
                    other_boxes = [el for el in self.caixas if el != caixa]

                    if (caixa[0], caixa[1] + 1) in other_boxes: #se caixa contra caixa
                        return False

        return True


    def arrumador_cima(self):
        arrumador_final = (self.arrumador[0] - 1, self.arrumador[1])

        if arrumador_final in self.paredes:
            return False

        for caixa in self.caixas:
            if caixa == arrumador_final:
                if (caixa[0] - 1, caixa[1]) in self.paredes:
                    return False

                if len(self.caixas) > 1:
                    other_boxes = [el for el in self.caixas if el != caixa]

                    if (caixa[0] - 1, caixa[1]) in other_boxes: #se caixa contra caixa
                        return False

        return True

    def arrumador_baixo(self):
        arrumador_final = (self.arrumador[0] + 1, self.arrumador[1])

        if arrumador_final in self.paredes:
            return False

        for caixa in self.caixas:
            if caixa == arrumador_final:
                if (caixa[0] + 1, caixa[1]) in self.paredes:
                    return False

                if len(self.caixas) > 1:
                    other_boxes = [el for el in self.caixas if el != caixa]

                    if (caixa[0] + 1, caixa[1]) in other_boxes: #se caixa contra caixa
                        return False

        return True

    def h1(self):
        total = 0
        for caixa in self.caixas:
            if caixa in self.alvos:
                total -= 5

            else:
                total += 5

        return total


    def h2(self):
        distancia = 0
        menor_distancia_alvo = 0
        num_walls = 0
        in_alvo = 0

        for caixa in self.caixas:
            #calcula distancia
            distancia_alvo = 0
            for alvo in range(len(self.alvos)):
                distancia_alvo = abs(caixa[0] - self.alvos[alvo][0]) + abs(caixa[1] - self.alvos[alvo][1])

                if alvo == 0:
                    menor_distancia_alvo = distancia_alvo

                elif distancia_alvo < menor_distancia_alvo:
                    menor_distancia_alvo = distancia_alvo

            distancia += menor_distancia_alvo

        return distancia + num_walls + in_alvo

    def h3(self):
        num_walls = 0

        for caixa in self.caixas:
            #calcula se esta em um canto
            if ((caixa[0] + 1, caixa[1]) in self.paredes and ((caixa[0], caixa[1] + 1) in self.paredes or (caixa[0], caixa[1] - 1) in self.paredes)):
                num_walls += 100

            elif ((caixa[0] - 1, caixa[1]) in self.paredes and ((caixa[0], caixa[1] + 1) in self.paredes or (caixa[0], caixa[1] - 1) in self.paredes)):
                num_walls += 100


        return num_walls
    

    def h4(self):
        distancia = 0
        menor_distancia_alvo = 0
        num_walls = 0
        in_alvo = 0

        for caixa in self.caixas:
            #calcula distancia
            distancia_alvo = 0
            for alvo in range(len(self.alvos)):
                distancia_alvo = abs(caixa[0] - self.alvos[alvo][0]) + abs(caixa[1] - self.alvos[alvo][1])

                if alvo == 0:
                    menor_distancia_alvo = distancia_alvo

                elif distancia_alvo < menor_distancia_alvo:
                    menor_distancia_alvo = distancia_alvo

            distancia += menor_distancia_alvo

            #calcula se esta em um canto
            if ((caixa[0] + 1, caixa[1]) in self.paredes and ((caixa[0], caixa[1] + 1) in self.paredes or (caixa[0], caixa[1] - 1) in self.paredes)):
                num_walls += 100

            elif ((caixa[0] - 1, caixa[1]) in self.paredes and ((caixa[0], caixa[1] + 1) in self.paredes or (caixa[0], caixa[1] - 1) in self.paredes)):
                num_walls += 100


            #calcula se caixa em alvos
            if caixa in self.alvos:
                in_alvo -= 2

            else:
                in_alvo += 2

        return distancia + num_walls + in_alvo

    def __str__(self) :
        string_to_return = ""
        d = {}

        for p in self.paredes:
            d[(p[0],p[1])] = "#"

        for c in self.caixas:
            d[(c[0],c[1])] = "*"

        for a in self.alvos:
            if (a[0],a[1]) in self.caixas:
                d[(a[0],a[1])] = "@"
            else:
                d[(a[0],a[1])] = "o"

        if self.arrumador in self.alvos:
            d[self.arrumador] = "B"

        else:
            d[self.arrumador] = "A"

        max_line = sorted(self.paredes)[-1]
        max_coll = sorted(self.paredes, key=lambda x: x[1])[-1]

        for line in range(max_line[0] + 1):
            for col in range(max_coll[1] + 1):
                if (line, col) in d.keys():
                    string_to_return += d[(line, col)]

                else:
                    string_to_return += "."

            string_to_return += "\n"

        return string_to_return


    def __eq__(self,estado):
        return self.caixas == estado.caixas and self.arrumador == estado.arrumador

    def __hash__(self):
        return hash((self.arrumador, self.caixas, self.paredes, self.alvos))

    def __lt__(self, estado):
        caixas_no_alvo_self = 0
        caixas_no_alvo_estado = 0

        for caixa in self.caixas:
            if caixa in self.alvos:
                caixas_no_alvo_self += 1

        for caixa in estado.caixas:
            if caixa in estado.alvos:
                caixas_no_alvo_estado += 1

        return caixas_no_alvo_self < caixas_no_alvo_estado


class Problema_sokoban(Problem):
    def __init__(self, inicial = Estado_sokoban()):
        super().__init__(inicial)

    def actions(self, estado):
        acoes = list()

        if estado.arrumador_esquerda():
            acoes.append("mover para a esquerda")

        if estado.arrumador_direita():
            acoes.append("mover para a direita")

        if estado.arrumador_cima():
            acoes.append("mover para cima")

        if estado.arrumador_baixo():
            acoes.append("mover para baixo")

        return acoes

    def result(self, estado, acao):
        arrumador = estado.arrumador
        caixas_final = []

        if acao == "mover para a esquerda":
            arrumador_final = (arrumador[0], arrumador[1] - 1)

            for caixa in estado.caixas:
                if arrumador_final == caixa:
                    caixas_final.append((caixa[0], caixa[1] - 1))
                else:
                    caixas_final.append(caixa)

            caixas_final = tuple(caixas_final)

            resultado = Estado_sokoban(arrumador_final, caixas_final, estado.paredes, estado.alvos)

        elif acao == "mover para a direita":
            arrumador_final = (arrumador[0], arrumador[1] + 1)

            for caixa in estado.caixas:
                if arrumador_final == caixa:
                    caixas_final.append((caixa[0], caixa[1] + 1))
                else:
                    caixas_final.append(caixa)

            caixas_final = tuple(caixas_final)

            resultado = Estado_sokoban(arrumador_final, caixas_final, estado.paredes, estado.alvos)

        elif acao == "mover para cima":
            arrumador_final = (arrumador[0] - 1, arrumador[1])

            for caixa in estado.caixas:
                if arrumador_final == caixa:
                    caixas_final.append((caixa[0] - 1, caixa[1]))
                else:
                    caixas_final.append(caixa)

            caixas_final = tuple(caixas_final)

            resultado = Estado_sokoban(arrumador_final, caixas_final, estado.paredes, estado.alvos)

        elif acao == "mover para baixo":
            arrumador_final = (arrumador[0] + 1, arrumador[1])

            for caixa in estado.caixas:
                if arrumador_final == caixa:
                    caixas_final.append((caixa[0] + 1, caixa[1]))
                else:
                    caixas_final.append(caixa)

            caixas_final = tuple(caixas_final)

            resultado = Estado_sokoban(arrumador_final, caixas_final, estado.paredes, estado.alvos)

        else:
            raise Exception("Há aqui qualquer coisa mal>> acao não reconhecida")

        return resultado

    def goal_test(self, estado):
        global num_est_expand
        num_est_expand += 1

        for caixa in estado.caixas:
            if caixa not in estado.alvos:
                return False

        return True

    def h1(self, node):
        return node.state.h1()

    def h2(self, node):
        return node.state.h2()

    def h3(self, node):
        return node.state.h3()

    def h4(self, node):
        return node.state.h4()


def problem_from_file(file):
    paredes = []
    caixas = []
    alvos = []

    in_file = open(file, "r")

    all_lines = in_file.readlines()

    for line in range(len(all_lines)):
        for col in range(len(all_lines[line])):
            if all_lines[line][col] == "#":
                paredes.append((line, col))

            elif all_lines[line][col] == "A":
                arrumador = (line, col)

            elif all_lines[line][col] == "*":
                caixas.append((line, col))

            elif all_lines[line][col] == "o":
                alvos.append((line, col))

            elif all_lines[line][col] == "@":
                caixas.append((line, col))
                alvos.append((line, col))

            elif all_lines[line][col] == "B":
                arrumador = (line, col)
                alvos.append((line, col))

    in_file.close()

    return Problema_sokoban(Estado_sokoban(arrumador, tuple(caixas), tuple(paredes), tuple(alvos)))


def print_path(search):
    for node in search.path():
        print(node.state)
        

num_est_expand = 0
prob_sokoban = problem_from_file("puzzle1.txt")
print(prob_sokoban.initial)
print("****")

tent1 = greedy_best_first_graph_search(prob_sokoban, prob_sokoban.h4)
print(tent1.solution())
print(len(tent1.solution()))
print(num_est_expand)
# print_path(tent1)

num_est_expand = 0
tent2 = astar_search(prob_sokoban, prob_sokoban.h4)
print(tent2.solution())
print(len(tent2.solution()))
print(num_est_expand)
# print_path(tent2)

num_est_expand = 0
tent3 = depth_first_graph_search(prob_sokoban)
print(tent3.solution())
print(len(tent3.solution()))
print(num_est_expand)
# print_path(tent3)

num_est_expand = 0
tent4 = breadth_first_search(prob_sokoban)
print(tent4.solution())
print(len(tent4.solution()))
print(num_est_expand)
# print_path(tent4)
