source("R/is_valid_sequence.R")
trans2word <- function(x, valid_transitions) {
    assertthat::assert_that(is_valid_sequence(x, valid_transitions), msg = "The sequence of transitions is invalid.")
    X <- valid_transitions[, x]
    return(c(X[1,1], X[2,]))
}
