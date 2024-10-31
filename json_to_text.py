import json

def json_to_text():
    # Solicita o caminho do arquivo JSON
    caminho_json = input("Digite o caminho do arquivo JSON: ")
    
    # Solicita o caminho do arquivo de saída
    caminho_saida = input("Digite o caminho do arquivo de saída: ")

    try:
        with open(caminho_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            for item in dados:
                # Processa o artigo
                artigo = item.get("Artigo ", 0)

                # Se o artigo não for um número, usa 0 como padrão
                if isinstance(artigo, (int, float)):
                    artigo = int(artigo)
                else:
                    artigo = 0  # ou um valor padrão que você preferir

                # Processa outros campos, substituindo '-' por ''
                descricao = item.get("Descrição", "").replace('-', '')
                diametro = item.get("Diâmetro mm", "").replace('-', '')
                profundidade = item.get("Profundidade do furo ou de perfuração", "").replace('-', '')
                materia_prima = item.get("Matéria Prima", "").replace('-', '')
                norma_din = item.get("Norma DIN ", "").replace('-', '')
                norma_rosca = item.get("Norma da Rosca", "").replace('-', '')
                revestimento = item.get("Revestimento", "").replace('-', '')
                furo = item.get("Furo (Cego/Passante)", "").replace('-', '')
                type_form = item.get("Type/Form", "").replace('-', '')
                materiais = item.get("Materiais", "").replace('-', '')
                tipo_rosca = item.get("Tipo de Rosca (Cortada / Laminada)", "").replace('-', '')
                numero_facas = item.get("Número de facas", "").replace('-', '')
                forma_haste = item.get("Forma da Haste", "").replace('-', '')
                refrigeracao_interna = item.get("Refrigeração Interna", "").replace('-', '')

                texto = [
                    f"O artigo {artigo} é {descricao}",
                    f"O artigo {artigo} tem um diâmetro em mm de {diametro}",
                    f"O artigo {artigo} permite uma Profundidade do furo ou de perfuração {profundidade}",
                    f"O artigo {artigo} segue a Norma da Rosca {norma_rosca}",
                    f"O artigo {artigo} segue a Norma DIN {norma_din}",
                    f"O artigo {artigo} é usado para revestimento {revestimento}",
                    f"O artigo {artigo} usa a matéria-prima {materia_prima}",
                    f"O artigo {artigo} tem um furo (Cego/Passante) {furo}",
                    f"O artigo {artigo} tem um número de facas igual a {numero_facas}",
                    f"O artigo {artigo} tem tipo/forma {type_form}",
                    f"O artigo {artigo} tem tipo de Rosca {tipo_rosca}",
                    f"O artigo {artigo} tem forma da Haste {forma_haste}",
                    f"O artigo {artigo} tem refrigeração líquida {refrigeracao_interna}",
                    f"O artigo {artigo} é adequado para a furação dos seguintes materiais {materiais}"
                ]
                
                with open(caminho_saida, 'a', encoding='utf-8') as saida:
                    for linha in texto:
                        saida.write(linha + '\n')

        print(f"Saída escrita com sucesso em: {caminho_saida}")

    except FileNotFoundError:
        print("Erro: O arquivo JSON especificado não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formatado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

json_to_text()

# c:/Users/cesar/Downloads/resultado.json
# c:/Users/cesar/Downloads/saida.txt
