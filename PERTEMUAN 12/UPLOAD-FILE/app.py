from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'kuncirahasiaku'

# Tentukan folder untuk menyimpan file yang diupload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Tentukan ekstensi file yang diizinkan
EKSTENSI_DIIJINKAN = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'bmp'}

# Fungsi untuk memeriksa ekstensi file yang diupload
def ekstensi_diijinkan(namafile):
    return '.' in namafile and namafile.rsplit('.', 1)[1].lower() in EKSTENSI_DIIJINKAN

@app.route('/', methods=['GET', 'POST'])
def unggah_file():
    if request.method == 'POST':
        # Periksa apakah file ada dalam request
        if 'file' not in request.files:
            flash('Tidak ada bagian file')
            return redirect(request.url)
        file = request.files['file']
        # Jika tidak ada file yang dipilih
        if file.filename == '':
            flash('Tidak ada file yang dipilih')
            return redirect(request.url)
        # Jika file memiliki ekstensi yang diizinkan
        if file and ekstensi_diijinkan(file.filename):
            # Membuat folder jika belum ada
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            namafile = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(namafile)
            flash(f'File berhasil diunggah ke {namafile}')
            return redirect(request.url)
        else:
            flash('Tipe File Tidak Sesuai, yang diizinkan tipe (png, jpg, jpeg, gif, pdf, bmp)')
            return redirect(request.url)
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('unggah.html', files=files)

@app.route('/lihat/<filename>')
def lihat_file(filename):
    return redirect(url_for('static', filename=os.path.join(app.config['UPLOAD_FOLDER'], filename)))

if __name__ == '__main__':
    app.run(debug=True)