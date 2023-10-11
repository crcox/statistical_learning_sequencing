source("R/is_valid_sequence.R")
source("R/sequence_errors.R")
source("R/suggest_swap.R")
source("R/trans2word.R")
source("R/word2trans.R")

valid_transitions2 <- cbind(combn(1:4, 2), combn(1:4, 2)[c(2, 1), ])
n_transition_types2 <- ncol(valid_transitions)
transition_id2 <- seq_len(n_transition_types)

# Sanity check
all.equal(n_transition_types, choose(4, 2) * 2)


# In a valid sequence of 13 words spanning all 12 possible transitions, three
# words will be presented 3 times and one word will be presented 4 times.


valid_sequence <- list(
    transitions = c(1, 4, 6, 9, 2, 8, 3, 11, 5, 12, 10, 7)
)
valid_sequence$words <- trans2word(valid_sequence$transitions, valid_transitions)
lapply(valid_sequence, table)

# Behavior on a valid sequence of transitions
is_valid_sequence(valid_sequence$transitions, valid_transitions)
sequence_errors(valid_sequence$transitions, valid_transitions)
find_invalid_transition(valid_sequence$transitions, valid_transitions)
suggest_swap(valid_sequence$transitions, valid_transitions)

# Behavior on an invalid sequence of transitions
invalid_sequence <- list(transitions = 1:12)

is_valid_sequence(invalid_sequence$transitions, valid_transitions)
sequence_errors(invalid_sequence$transitions, valid_transitions)
find_invalid_transition(invalid_sequence$transitions, valid_transitions)
suggest_swap(invalid_sequence$transitions, valid_transitions)


(ix <- suggest_swap(invalid_sequence$transitions, valid_transitions))
while (!any(is.na(ix))) {
    invalid_sequence$transitions[ix] <- invalid_sequence$transitions[rev(ix)]
    (ix <- suggest_swap(invalid_sequence$transitions, valid_transitions))
}
is_valid_sequence(invalid_sequence$transitions, valid_transitions)
invalid_sequence$words <- trans2word(invalid_sequence$transitions, valid_transitions)


# Full scale attempt ----

x <- list(transitions = sample(rep(transition_id, 11 * 2)))

is_valid_sequence(x$transitions, valid_transitions)
sequence_errors(x$transitions, valid_transitions)

# Iterate towards a valid sequence
ix <- suggest_swap(x$transitions, valid_transitions)
while (!any(is.na(ix))) {
    x$transitions[ix] <- x$transitions[rev(ix)]
    ix <- suggest_swap(x$transitions, valid_transitions)
}
is_valid_sequence(x$transitions, valid_transitions)
x$words <- trans2word(x$transitions, valid_transitions)

lapply(x, table)

# write index to csv
cudir <- getwd()
filename <- paste(cudir, "/indices.csv", sep = "")
write.csv(x$words, filename)
