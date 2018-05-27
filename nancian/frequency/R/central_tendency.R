'
Medidas de frequência central

OBS: Não está sendo utilizado funções prontas da linguagem
para que haja entendimento de minha parte.

Os nomes das funções seguem o padrão definido na lista de exercícios.
'

# Função para calcular a média aritmética
x <- function(arr) {
  return (sum(arr) / length(arr));
}

# Função para encontrar a mediana
md <- function(arr) {
  arr <- sort(arr);
  if ((length(arr) %% 2) == 0) {
    return((arr[((length(arr)/2))] + arr[((length(arr)/2) + 1)]) / 2);
  } else {
    return(arr[length(arr) / 2]);
  }
}

# Função para encontrar a moda
mo <- function(arr) { 
   unique_values <- unique(arr);
   unique_values[which.max(tabulate(match(arr, unique_values)))];
}
