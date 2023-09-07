function confirmarDeleteAluguel(id) {
    if(confirm('Deseja realmente excluir esse cadastro?') == true) {
        window.location.href="aluguel_delete/" + id;
    }
}