let total = null;
async function getFiles(){
    const main = document.querySelector('main')
    const response = await fetch('/files');
    const files = await response.json();
    
    if(files.length === 0){
        console.log('No files found');
        main.innerHTML = '<h1>No files found</h1>';
        return;

    }

    if (total === files.length){
        console.log('No changes');
        return;
    }

    main.innerHTML = '';
    files.forEach(file => {
        const card = document.createElement('card-file');
        card.setAttribute('file-type', file.original_file.split('.')[1]);
        card.setAttribute('file-name', file.original_file.split('.')[0]);
        card.setAttribute('file-local', file.id)

        main.appendChild(card);
    });
}


document.addEventListener('DOMContentLoaded', getFiles);