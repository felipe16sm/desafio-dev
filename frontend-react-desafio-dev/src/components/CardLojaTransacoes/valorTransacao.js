export const valorTransacao = (transacao) => {
  if (
    transacao.tipo === 1 ||
    transacao.tipo === 4 ||
    transacao.tipo === 5 ||
    transacao.tipo === 6 ||
    transacao.tipo === 7 ||
    transacao.tipo === 8
  ) {
    return Number(transacao.valor);
  }

  if (transacao.tipo === 2 || transacao.tipo === 3 || transacao.tipo === 9) {
    return -Number(transacao.valor);
  }
};
