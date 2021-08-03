import {
  Card,
  CardActionArea,
  CardContent,
  makeStyles,
  Typography,
} from "@material-ui/core";

import {
  formatCPF,
  formatData,
  formatHorario,
  identificaTransacao,
} from "./formatacoes";
const useStyles = makeStyles({
  root: {
    margin: "5px",
    width: 300,
  },
});

export const CardTransacao = ({ transacaoData }) => {
  const classes = useStyles();
  return (
    <>
      <Card className={classes.root}>
        <CardActionArea>
          <CardContent>
            <Typography color="primary" component="h4">
              Tipo: {transacaoData.tipo} -{" "}
              {identificaTransacao(transacaoData.tipo)}
            </Typography>
            <Typography color="primary" component="h4">
              Cartão: {transacaoData.cartao}
            </Typography>
            <Typography color="primary" component="h4">
              CPF: {formatCPF(transacaoData.cpf)}
            </Typography>
            <Typography color="primary" component="h4">
              Data: {formatData(transacaoData.data)}
            </Typography>
            <Typography color="primary" component="h4">
              Hora: {formatHorario(transacaoData.hora)}
            </Typography>
            <Typography color="primary" component="h4">
              Valor: R$ {transacaoData.valor.toFixed(2)}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </>
  );
};
