// use std::env;
use std::fs;

pub fn puzzle_a() {
    println!("\n\n==== Day 01 ====");
    println!("-- Puzzle A --");
    // ------------------------------------------------------------------------

    let contents = fs::read_to_string("day_01/01_input.txt").unwrap();
    let result = find_number_of_increases(&contents);

    println!("Result:\n{:?}", result);

    // ------------------------------------------------------------------------
}

fn find_number_of_increases<'a>(input: &'a str) -> i32 {
    let mut numbers = Vec::new();
    for line in input.lines() {
        let num: i32 = line.parse().unwrap();
        numbers.push(num);
    }

    let mut sum = 0;
    for (i, _x) in numbers.iter().enumerate() {
        sum = if (i != 0) && numbers[i] > numbers[i - 1] {
            sum + 1
        } else {
            sum
        }
    }

    return sum;
}

pub fn puzzle_b() {
    println!("\n-- Puzzle B --");
    // ------------------------------------------------------------------------

    let contents = fs::read_to_string("day_01/01_input.txt").unwrap();
    let result = find_number_of_window_increases(&contents);

    println!("Result:\n{:?}", result);

    // ------------------------------------------------------------------------
}

fn sum3(vec: Vec<i32>, end: usize) -> i32 {
    return vec[end - 2] + vec[end - 1] + vec[end];
}

fn find_number_of_window_increases<'a>(input: &'a str) -> i32 {
    let mut numbers = Vec::new();
    for line in input.lines() {
        let num: i32 = line.parse().unwrap();
        numbers.push(num);
    }

    let mut sum = 0;
    // println!("Letter\tSum\tChange",);
    // println!("---------------------------",);
    for (i, _x) in numbers.iter().enumerate() {
        // let letters = ["A", "B", "C", "D", "E", "F", "G", "H"];
        // let letter = if i > 2 { letters[i - 3] } else { "" };
        // let mut change = "";
        sum = if (i > 2)
            && (sum3(numbers.clone(), i) > sum3(numbers.clone(), i - 1))
        {
            // change = "Increase";
            sum + 1
        } else {
            sum
        };
        // if i > 2 {
        //     println!(
        //         "{}\t{:?}\t{:?}",
        //         letter,
        //         sum3(numbers.clone(), i),
        //         change
        //     );
        // }
    }

    return sum;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn puzzle_a() {
        let contents = fs::read_to_string("day_01/01_test_input.txt").unwrap();
        let result = find_number_of_increases(&contents);
        assert_eq!(result, 7);
    }
    #[test]
    fn puzzle_b() {
        let contents = fs::read_to_string("day_01/01_test_input.txt").unwrap();
        let result = find_number_of_window_increases(&contents);
        assert_eq!(result, 5);
    }
}
