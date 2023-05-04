class CardElement extends HTMLElement
{
    constructor(){
        super()
        this.attachShadow({ mode: "open" })
    }

    connectedCallback(){
        const fileLocation = this.getAttribute('file-local')
        const fileName = this.getAttribute('file-name')
        const fileType = this.getAttribute('file-type')
        
        this.style.width = 'clamp(230px, 28%, 280px)'
        
        this.shadowRoot.innerHTML = `
            <style>
            .card
            {
                width: clamp(230px, 28%, 280px);
                margin: 20px;
                padding: 10px;
                border-radius: 10px;
                background-color: #90f1b2;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: flex-start;
            }
            
            .card > h2
            {
                font-size: 1.5rem;
                color: #000b;
                margin-bottom: 20px;
                text-transform: uppercase;
                width: 100%;
                text-overflow: ellipsis;
                overflow: hidden;
                text-align: center;
            }
            
            .card > span.type{
                font-size: 1.2rem;
                color: #0007;
                margin-bottom: 30px;
                text-transform: uppercase;
            }
            
            .card > button
            {
                width: calc(80% - 40px);
                border: solid 2px #14715c;
                border-radius: 10px;
                color: #14715c;
                background-color: transparent;
                padding: 10px 20px;
                margin: 5px 0;
                cursor:pointer;
            }

            .remove{
                color: #fff !important;
                border: 0 !important;
                background-color: #b82a42 !important;
            }
            </style>
            <div class="card">
                <h2>${fileName}</h2>
                <span class="type">${fileType}</span>

                <button onclick='location.href="/files/${fileLocation}/download"' class="download">
                    Baixar
                </button>

                <button class='remove' onclick='delete_file(${fileLocation})'>
                    Apagar Permanentemente
                </button>
            </div>
        `
    }
}

customElements.define("card-file", CardElement);