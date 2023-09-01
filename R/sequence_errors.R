sequence_errors <- function(x, valid_transitions) {
    n <- length(x)
    e <- 0
    v <- valid_transitions[1, ]
    for (i in seq_len(n - 1)) {
        cur <- valid_transitions[2, x[i]]
        valid_ids <- which(cur == v)
        e <- e + !(x[i + 1] %in% valid_ids)
    }
    return(e)
}
