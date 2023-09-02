word2trans <- function(x, valid_transitions) {
    n <- length(x)
    X <- rbind(x[1:(n-1)], x[2:n])
    trans <- numeric(ncol(X))
    for (i in seq_len(ncol(valid_transitions))) {
        z <- which(apply(valid_transitions[, i] == X, 2, all))
        trans[z] <- i
    }
}
