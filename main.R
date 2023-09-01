valid_transitions <- cbind(combn(1:4, 2), combn(1:4, 2)[c(2,1), ])
n_transition_types <- ncol(valid_transitions)
transition_id <- seq_len(n_transition_types)

# Sanity check
all.equal(n_transition_types, choose(4,2) * 2)

x <- rep(transition_id, 11)

# In a valid sequence of 13 words spanning all 12 possible transitions, three
# words will be presented 3 times and one word will be presented 4 times.
valid_sequence <- c(1,4,6,9,2,8,3,11,5,12,10,7)
table(c(1, valid_transitions[2, valid_sequence]))
table(valid_transitions[2, ])

# Behavior on a valid sequence of transitions
is_valid_sequence(valid_sequence, valid_transitions)
sequence_errors(valid_sequence, valid_transitions)
find_invalid_transition(valid_sequence, valid_transitions)
suggest_swap(valid_sequence, valid_transitions)

# Behavior on an invalid sequence of transitions
invalid_sequence <- 1:12
is_valid_sequence(invalid_sequence, valid_transitions)
sequence_errors(invalid_sequence, valid_transitions)
find_invalid_transition(invalid_sequence, valid_transitions)
ix <- suggest_swap(invalid_sequence, valid_transitions)
if (!any(is.na(ix))) {
    invalid_sequence[ix] <- invalid_sequence[rev(ix)]
} else if (length(ix) > 1 && is.na(ix[2])) {
    a <- ix[1] - 1
    b <- ix[1]
    cur <- valid_transitions[2, invalid_sequence[a]]
    v <- which(cur == valid_transitions[1,])
    suggestions <- sample(which(invalid_sequence %in% v))
    for (i in seq_along(suggestions)) {
        p <- suggestions[i]
    }

}
find_invalid_transition(invalid_sequence, valid_transitions)

e <- sequence_errors(x, valid_transitions)
N <- length(x)
while (e > 0) {
    ix <- suggest_swap(x, valid_transitions)
    if (!any(is.na(ix))) x[ix] <- x[rev(ix)]
}

    x_swp[c(ix[2], ix[1])] <- x[ix]
    e_swp <- sequence_errors(x_swp, valid_transitions)
    if (e_swp < e) {
        x <- x_swp
        e <- e_swp
    }
