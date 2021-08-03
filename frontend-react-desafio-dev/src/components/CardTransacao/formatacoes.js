export const formatCPF = (cpf) => {
  return `${cpf.slice(0, 3)}.${cpf.slice(3, 6)}.${cpf.slice(6, 9)}-${cpf.slice(
    9,
    11
  )}`;
};

export const formatData = (data) => {
  const ano = data.slice(0, 4);
  const mes = data.slice(4, 6);
  const dia = data.slice(6, 8);
  return `${dia}/${mes}/${ano}`;
};

export const formatHorario = (horario) => {
  const horas = horario.slice(0, 2);
  const minutos = horario.slice(2, 4);
  const segundos = horario.slice(4, 6);

  return `${horas}:${minutos}:${segundos}`;
};

export const identificaTransacao = (idTransacao) => {
  if (idTransacao === 1) {
    return "Débito";
  }
  if (idTransacao === 2) {
    return "Boleto";
  }
  if (idTransacao === 3) {
    return "Financiamento";
  }
  if (idTransacao === 4) {
    return "Crédito";
  }
  if (idTransacao === 5) {
    return "Recebimento Empréstimo";
  }
  if (idTransacao === 6) {
    return "Vendas";
  }
  if (idTransacao === 7) {
    return "Recebimento TED";
  }
  if (idTransacao === 8) {
    return "Recebimento DOC";
  }
  if (idTransacao === 9) {
    return "Aluguel";
  }
};
