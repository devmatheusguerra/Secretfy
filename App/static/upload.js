async function upload_file()
{
    const file = await document.createElement('input');
    file.type = await 'file';
    await file.click();
    file.onchange = () => {
        const formData = new FormData();
        formData.append('file', file.files[0]);
        fetch('/files', {method: 'POST', body: formData})
            .then(response => {
                if (response.status == 201) {
                    alert('Upload successful');
                    getFiles()
                } else {
                    alert('Upload failed');
                }
            })
            .catch(error => {
                console.error(error);
            });
    }
}