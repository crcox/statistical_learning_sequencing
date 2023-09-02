#' Suggest a swap to move towards a valid sequence of transitions
#'
#' In an effort to enforce a strict balance of transition types in an artificial
#' grammar, we may start by defining a sequence of transitions that has an equal
#' number of each each transition type. The challenge, then, is to permute the
#' sequence of transitions so that the second element of the first transition
#' pair matches the first element of the second transition pair, and so on.
#'
#' @param x A sequence of transition ids
#' @param valid_transitions A matrix with a column for each valid transition. Transition ids in \code{x} refer to columns of x.
#' @returns A numeric pair for
#'
#' @details
#' The procedure implemented here considers each transition in order, checks if
#' subsequent transition is compatible with it, and if not suggests a swap that
#' replaces the incompatible transition with a compatible one later in the
#' sequence.
#'
#' If zero "swap suggestions" can be found later in the sequence, the function
#' will then look to an earlier point in the sequence for a compatible
#' transition to swap with. This swap will only be suggested if it does not
#' produce incompatible transitions.
#'
#' This function is intended to be called in a loop that iteratively applies the
#' suggested swaps until a valid sequence of transitions is obtained. It may be
#' possible that this optimization procedure leads to a dead end where no legal
#' swaps are possible and the sequence of transitions is invalid. At that point,
#' the only thing to do is reshuffle the sequence of transitions and start over.
#'
suggest_swap <- function(x, valid_transitions) {
    n <- length(x)
    w1_all <- valid_transitions[1, ]
    for (trans_i in seq_len(n - 1)) {
        trans_i_w2 <- valid_transitions[2, x[trans_i]]
        valid_ids <- which(trans_i_w2 == w1_all)
        if (!(x[trans_i + 1] %in% valid_ids)) {
            suggestions <- (trans_i + 1) + which(x[(trans_i + 2):n] %in% valid_ids)
            if (length(suggestions) > 0) {
                return(c(trans_i + 1, sample(suggestions, 1)))
            } else {
                suggestions <- which(x[1:(trans_i - 1)] %in% valid_ids)
                for (j in seq_along(suggestions)) {
                    trans_j <- suggestions[j]
                    trans_jm1_w2 <- valid_transitions[2, x[trans_j - 1]]
                    trans_j_w1 <- valid_transitions[1, x[trans_j]]
                    trans_j_w2 <- valid_transitions[2, x[trans_j]]
                    trans_jp1_w1 <- valid_transitions[1, x[trans_j + 1]]
                    if (
                        ((length(trans_jm1_w2) == 0) ||
                            (trans_jm1_w2 == trans_j_w1)) &&
                        (trans_j_w2 == trans_jp1_w1)
                    ) {
                        return(c(trans_j, trans_i + 1))
                    }
                }
                return(c(i + 1, NA))
            }
        }
    }
    return(NA)
}
