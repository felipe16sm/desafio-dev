import React from "react";
import {
  Card,
  CardActionArea,
  CardContent,
  makeStyles,
  Typography,
} from "@material-ui/core";

import { useHistory } from "react-router-dom";

const useStyles = makeStyles({
  root: {
    margin: "0 auto",
    marginTop: "10px",
    maxWidth: 345,
  },
});

export const CardLoja = ({ lojaData }) => {
  const classes = useStyles();
  const history = useHistory();

  const handleLojaData = () => {
    history.push("/loja-transacoes/" + lojaData.id);
  };

  return (
    <Card className={classes.root}>
      <CardActionArea onClick={handleLojaData}>
        <CardContent>
          <Typography component="h2">{lojaData.nome_loja}</Typography>
          <Typography color="textSecondary" component="h3">
            {lojaData.dono_loja}
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
};
