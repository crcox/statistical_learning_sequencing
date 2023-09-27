source("R/is_valid_sequence.R")
source("R/sequence_errors.R")
source("R/suggest_swap.R")
source("R/trans2word.R")
source("R/word2trans.R")

valid_transitions <- cbind(combn(1:12, 2), combn(1:12, 2)[c(2,1), ])
n_transition_types <- ncol(valid_transitions)
transition_id <- seq_len(n_transition_types)

# Sanity check
all.equal(n_transition_types, choose(12,2) * 2)


# Full scale attempt ----

x <- list(transitions = sample(rep(transition_id, 2)))

is_valid_sequence(x$transitions, valid_transitions)
sequence_errors(x$transitions, valid_transitions)

# Iterate towards a valid sequence
ix <- suggest_swap(x$transitions, valid_transitions)
while (!any(is.na(ix))) {
    x$transitions[ix] <- x$transitions[rev(ix)]
    ix <- suggest_swap(x$transitions, valid_transitions)
    cat(sequence_errors(x$transitions, valid_transitions), "\n")
}
is_valid_sequence(x$transitions, valid_transitions)
x$words <- trans2word(x$transitions, valid_transitions)

lapply(x, table)
