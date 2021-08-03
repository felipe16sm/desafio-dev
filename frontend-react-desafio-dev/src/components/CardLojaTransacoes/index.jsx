import { useEffect, useState } from "react";
import { api } from "../../api";
import { CardTransacao } from "../../components/CardTransacao";
import {
  Card,
  CardActionArea,
  CardContent,
  makeStyles,
  Typography,
} from "@material-ui/core";

import { valorTransacao } from "./valorTransacao";

const useStyles = makeStyles({
  root: {
    margin: "0 auto",
    marginTop: "10px",
    maxWidth: 345,
  },
  transacoesTitle: {
    textAlign: "center",
  },
  transacoesContainer: {
    margin: "0 auto",
    width: "90%",
    display: "flex",
    flexWrap: "wrap",
    justifyContent: "center",
    alignItems: "center",
  },
});

export const CardLojaTransacoes = ({ idLoja }) => {
  const classes = useStyles();
  const [lojaData, setLojaData] = useState("");

  useEffect(() => {
    api
      .get(`/stores/${idLoja}/transactions/`)
      .then((response) => {
        console.log(response.data);
        setLojaData(response.data);
      })
      .catch((error) => {
        console.log(error.response);
      });
  }, []);

  return (
    <>
      {lojaData && (
        <Card className={classes.root}>
          <CardActionArea>
            <CardContent>
              <Typography component="h2">{lojaData.nome_loja}</Typography>
              <Typography color="textSecondary" component="h3">
                {lojaData.dono_loja}
              </Typography>
            </CardContent>
          </CardActionArea>
        </Card>
      )}
      (
      <Card className={classes.root}>
        <CardActionArea>
          <CardContent>
            <Typography color="textPrimary" component="h3">
              Saldo em conta: R${" "}
              {lojaData &&
                lojaData.transacoes
                  .reduce((acum, current) => {
                    return acum + valorTransacao(current);
                  }, 0)
                  .toFixed(2)}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
      <h2 className={classes.transacoesTitle}>Transações</h2>
      <div className={classes.transacoesContainer}>
        {lojaData &&
          lojaData.transacoes.map((transacaoData, index) => {
            return <CardTransacao transacaoData={transacaoData} key={index} />;
          })}
      </div>
    </>
  );
};
