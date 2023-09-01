is_valid_sequence <- function(x, valid_transitions) {
    n <- length(x)
    v <- valid_transitions[1, ]
    for (i in seq_len(n - 1)) {
        cur <- valid_transitions[2, x[i]]
        valid_ids <- which(cur == v)
        if (!(x[i + 1] %in% valid_ids)) {
            return(FALSE)
        }
    }
    return(TRUE)
}

find_invalid_transition <- function(x, valid_transitions) {
    n <- length(x)
    v <- valid_transitions[1, ]
    for (i in seq_len(n - 1)) {
        cur <- valid_transitions[2, x[i]]
        valid_ids <- which(cur == v)
        if (!(x[i + 1] %in% valid_ids)) {
            return(i)
        }
    }
    return(0)
}
