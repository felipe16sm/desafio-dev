import { useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { api } from "../../api";
import { Button, makeStyles } from "@material-ui/core";

const useStyles = makeStyles({
  transactionContainer: {
    width: "40%",
    margin: "10px auto",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column",
  },
  button: {
    margin: "10px",
  },
  img: {
    display: "block",
    width: "150px",
    height: "150px",
  },
});

export const FormRegistrarTransacoes = () => {
  const classes = useStyles();
  const history = useHistory();
  const [data, setData] = useState(new FormData());
  const [selectedFile, setSelectedFile] = useState("");

  const handleRegisterTransactions = (e) => {
    const localData = data;
    localData.append("file", e.target.files[0]);
    console.log(e.target.files[0]);
    setSelectedFile(e.target.files[0].name);
    setData(localData);
  };

  const buttonRegisterTransactions = () => {
    api
      .post("stores/transactions/", data)
      .then((response) => {
        console.log(response);
        history.push("/lojas");
      })
      .catch((error) => {
        console.log(error.response);
      });
  };

  return (
    <div className={classes.transactionContainer}>
      <Button
        size="small"
        variant="contained"
        component="label"
        className={classes.button}
      >
        Selecione o arquivo com as transações
        <input
          id="files"
          type="file"
          hidden
          onChange={handleRegisterTransactions}
        />
      </Button>
      <div>{selectedFile}</div>
      <Button
        variant="contained"
        color="primary"
        onClick={buttonRegisterTransactions}
        className={classes.button}
      >
        Registrar transações
      </Button>
    </div>
  );
};
