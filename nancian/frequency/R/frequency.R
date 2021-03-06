'
DISTRIBUIÇÃO DE FREQÜÊNCIAS

Funções para solucionar os problemas propostos nas aulas
de estatística

Não estou usando muitas funções da linguagem para não compromenter meu aprendizado =D
'

# Cria a estrutura básica da tabela de distribuição de frequência
tabled <- function(arr){
  i <- c(arr);
  return(i);
}

# Função para gerar frequências
# Faz o calculo da frequencia simples ou absoluta
frequency_simple <- function(arr) {
  fi <- c();
  arr <- sort(arr); # Ordenando elementos
  unique_values <- unique(arr); # Removendo elementos duplicados
  for (unique_value in unique_values) {
    cont <- 0;
    for (value in arr) {
      if (unique_value == value) {
        cont <- cont + 1;
      }
    }
    fi <- c(fi, cont);
  }
  return(fi);
}

# Função para calcular a frequência acumulada
function_acumulate <- function(fi) {
  Fi <- c(0);
  for (value in fi) {
    Fi <- c(Fi, value + tail(Fi, n=1))
  }
  # Retorna todos os elementos menos o primeiro
  return(tail(Fi, n=-1));
}

# Função para calcular a frequência relativa
function_relative <- function(fi) {
  somatorio = sum(fi);
  fri <- c();
  for (value in fi) {
    fri <- c(fri, value / somatorio);
  }
  return (fri);
}

# Função para calcular a frequência acumulada relativa
function_acumulate_relative <- function(fri) {
  Fri <- c(0);
  for (value in fri) {
    Fri <- c(Fri, value + tail(Fri, n = 1));
  }
  return(tail(Fri, n=-1));
}

# Devolve tabela montada com todas as informações
# Devolve o DataFrame completo
visualize_table <- function(i, elements, fi, Fi, fri, Fri) {
  return(data.frame(i, elements, fi, Fi, fri, Fri));
}

# Função para solução de distribuições de frequência por completo
frequency_distribuition <- function(arr) {
  fi <- frequency_simple(arr);
  Fi <- function_acumulate(fi);
  fri <- function_relative(fi);
  Fri <- function_acumulate_relative(fri);
  visualize_table(1:length(unique(arr)), unique(arr), fi, Fi, fri, Fri);
}
