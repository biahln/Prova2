def get_idcadastro(cursor, url, codigo):
    cursor.execute(f'select idcadastro from cod where url ="{url}" and codigo="{codigo}"')

    idcadastro = cursor.fetchone()
    cursor.close()
    return idcadastro


