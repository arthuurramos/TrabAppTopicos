import sqlite3 as lite

# conexão com bd
con = lite.connect('dados.db')

# inserir CATEGORIA
def inserirCategoria(i):
    with con:
        cur  = con.cursor()
        query = "INSERT INTO Categoria(nome) VALUES (?)"
        cur.execute(query, i)

# inserir RECEITAS
def inserirReceita(i):
    with con:
        cur  = con.cursor()
        query = "INSERT INTO Receitas(categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

# inserir GASTOS
def inserirGastos(i):
    with con:
        cur  = con.cursor()
        query = "INSERT INTO Gastos(categoria, retirado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

#############################################################################

# DELETAR Receitas
def deletarReceitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas WHERE id=?"
        cur.execute(query, i)

def deletarGastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos WHERE id=?"
        cur.execute(query, i)

#############################################################################
        
# Ver Categorias
def verCategorias():
        
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

# Ver Receitas
def verReceitas():
        
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens


# Ver Gastos
def verGastos():
        
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens
