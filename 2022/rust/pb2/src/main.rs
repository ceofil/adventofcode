use std::fs;


fn score(line: &str) -> i32 {
    let words: Vec<&str> = line.split(" ").collect();
    let a = words[0];
    let b = words[1];

    let win_score = match b {
       "X" => 0,
       "Y" => 3,
       "Z" => 6,
       &_ => todo!()
    };

    let choice: &str = match (a, win_score){
        ("A", 6) => "paper",
        ("A", 3) => "rock",
        ("B", 3) => "paper",
        ("B", 0) => "rock",
        ("C", 0) => "paper",
        ("C", 6) => "rock",
        (&_, _) => "scissors"
    };

    let choice_score = match choice {
        "rock" => 1,
        "paper" => 2,
        "scissors" => 3,
        &_ => todo!()
    };

    println!("{},{},{},{}", a, b, win_score, choice_score);
    return choice_score + win_score;
}
fn main() {
    let contents = fs::read_to_string("input").expect("correct input");
    let suma: i32 = contents.split("\n").map(
        |line| score(line)
    ).sum();
    println!("{}", suma)
}
