suggest_swap <- function(x, valid_transitions) {
    n <- length(x)
    v <- valid_transitions[1, ]
    for (i in seq_len(n - 1)) {
        cur <- valid_transitions[2, x[i]]
        valid_ids <- which(cur == v)
        if (!(x[i + 1] %in% valid_ids)) {
            suggestions <- (i + 1) + which(x[(i + 2):n] %in% valid_ids)
            if (length(suggestions) > 0) {
                return(c(i + 1, sample(suggestions, 1)))
            } else {
                return(c(i + 1, NA))
            }
        }
    }
    return(NA)
}
