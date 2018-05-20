'
  Funções para cálculo de probabilidade
  
  Aqui quase nenhuma função pronta está sendo utilizada, para que eu aprenda ao máximo
a lógica dos exercícios
'

#' Função para realizar cálculos de probabilidade simples
#' @param cf_a Casos favoraveis ao evento A ocorrer
#' @param space Espaço amostral 
#' @return Devolve a porcentagem de chances do evento ocorrer
prob_simple <- function(cf_a, space) {
  return((cf_a / space) * 100); 
}

#' Função para calcular a probabilidade com o teorema da soma
#' @param p_a Probabilidade do evento A ocorrer
#' @param p_b Probabilidade do evento B ocorrer
#' @param p_ab Probabilidade do evento A e B ocorrer
#' @return Retorna a probabilidade (Porcento) de um dos eventos ocorrer 
prob_sum <- function(p_a, p_b, p_ab) {
  return(((p_a + p_b) -p_ab) * 100);   
}

#' Função para calcular a probabilidade com o teorema do produto
#' @param p_a Probabilidade do evento A ocorrer
#' @param p_b Probabilidade do evento B ocorrer
#' @return Retorna a probabilidade (Porcento) dos dois eventos ocorrer
prob_prod <- function(p_a, p_b) {
  return((p_a * p_b) * 100);
}

#' Função que aplica a união dos teoremas (Produto e Soma) para a solução do exercício.
#' Para que se entenda a função veja o exemplo de onde esta pode ser aplicada:
#' A probabilidade de que Pedro resolva um problema é de 1/3 e a de que Paulo resolva é 1/4, se ambos
#' tentarem independentemente resolver, qual a probabilidade de que o problema seja resolvido ?
#' Perceba que, neste caso a ideia é cálcular a probabilidade de algo ocorrer, independente de qual lado
#' a solução virá.
#' @param p_a Probabilidade do evento A ocorrer
#' @param p_b Probabilidade do evento B ocorrer
#' @return Retorna a probabilidade (Porcento) do evento ocorrer
prob_solver <- function(p_a, p_b) {
  # P(E) = (P(A) + P(B)) - (P(A) * P(B))
  return(((p_a + p_b) - (p_a * p_b)) * 100);
} 
