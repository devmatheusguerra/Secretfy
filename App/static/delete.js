async function delete_file(id) {
    if (!confirm("Realmente deseja apagar o arquivo? Não será possível recuperá-lo!")) { return };
    const response = await fetch("/files/" + id + "/delete", { method: "DELETE" })
    if (response.status == 200) {
        getFiles()
    } else if (response.status == 404) {
        alert("Arquivo não encontrado")
    } else {
        alert("Erro ao apagar arquivo")
    }
}