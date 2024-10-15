from flask import Flask
import xml.dom.minidom as minidom

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def main():
    # Gunakan fungsi parse() untuk me-load XML ke memori dan melakukan parsing
    try:
        doc = minidom.parse("mahasiswa.xml")

        # Cetak isi doc dan tag pertamanya
        print(doc.nodeName)
        print(doc.firstChild.tagName)

        # Ambil data dari XML
        nama = doc.getElementsByTagName("nama")[0].firstChild.data
        alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
        jurusan = doc.getElementsByTagName("jurusan")[0].firstChild.data
        list_hobi = doc.getElementsByTagName("hobi")

        # Cetak data ke terminal
        output = f"Nama: {nama}\nAlamat: {alamat}\nJurusan: {jurusan}\n"
        output += f"Memiliki {len(list_hobi)} hobi:\n"

        for hobi in list_hobi:
            output += f"- {hobi.getAttribute('name')}\n"

        print(output)

        # Return output sebagai response
        return output

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

if __name__ == "__main__":
    app.run()
