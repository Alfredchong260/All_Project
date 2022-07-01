package main

import (
	"fmt"
	"strings"
	"time"
  "sync"
)

const conferenceTicket int = 50

var conferenceName string = "Go Conference"
var remainingTickets uint = 50
var bookings = make([]UserData, 0)

type UserData struct {
	firstName       string
	lastName        string
	email           string
	numberOfTickets uint
}

var wg = sync.WaitGroup{}

func main() {

	greetUsers()

	for remainingTickets > 0 && len(bookings) < 50 {

		firstName, lastName, email, userTickets := getUserInput()
		isValidName, isValidEmail, isValidTicketNum := validateUserInput(firstName, lastName, email, userTickets)

		if isValidName && isValidEmail && isValidTicketNum {

			bookTicket(userTickets, firstName, lastName, email)

      wg.Add(1)
      go sendTicket(userTickets, firstName, lastName, email)
			firstNames := printFirstNames()

			fmt.Printf("The first name of bookings are : %v\n\n", firstNames)

			if remainingTickets == 0 {
				fmt.Println("Our conference is booked out. Come back next year.")
				break
			}

		} else {
			if !isValidName {
				fmt.Println("First name or last name entered too short")
			}

			if !isValidEmail {
				fmt.Println("email address you entered doesn't have @ sign")
			}

			if !isValidTicketNum {
				fmt.Println("number of tickets you entered is invalid")
			}
		}

	}
  wg.Wait()
}

func greetUsers() {

	fmt.Printf("Welcome to %v bookings application.\n", conferenceName)
	fmt.Printf("We have total %v tickets and %v are still available,\n", conferenceTicket, remainingTickets)
	fmt.Println("Get your ticker here to attend.")

}

func printFirstNames() []string {

	firstNames := []string{}

	for _, booking := range bookings {
		firstNames = append(firstNames, booking.firstName)
	}

	return firstNames
}

func getUserInput() (string, string, string, uint) {

	var firstName string
	var lastName string
	var email string
	var userTickets uint

	fmt.Print("Please enter your first name :")
	fmt.Scan(&firstName)
	fmt.Print("Please enter your last name :")
	fmt.Scan(&lastName)
	fmt.Print("Please enter your email address :")
	fmt.Scan(&email)
	fmt.Print("Please enter number of ticket(s) you want to book :")
	fmt.Scan(&userTickets)

	return firstName, lastName, email, userTickets
}

func bookTicket(userTickets uint, firstName string, lastName string, email string) {

	remainingTickets -= userTickets

	var userData = UserData{
		firstName:       firstName,
		lastName:        lastName,
		email:           email,
		numberOfTickets: userTickets,
	}

	// userData["firstName"] = firstName
	// userData["lastName"] = lastName
	// userData["email"] = email
	// userData["numberOfTickets"] = strconv.FormatUint(uint64(userTickets), 10)

	bookings = append(bookings, userData)

	fmt.Printf("Thank you %v %v for bookings %v tickets.\nYou will receive a confirmation email at %v\n", firstName, lastName, userTickets, email)
	fmt.Printf("%v tickets remaining for %v\n", remainingTickets, conferenceName)
}

func validateUserInput(firstName string, lastName string, email string, userTickets uint) (bool, bool, bool) {
	isValidName := len(firstName) >= 2 && len(lastName) >= 2
	isValidEmail := strings.Contains(email, "@")
	isValidTicketNum := userTickets > 0 && userTickets <= remainingTickets

	return isValidName, isValidEmail, isValidTicketNum
}


func sendTicket(userTickets uint, firstName string, lastName string, email string)  {
  var ticket = fmt.Sprintf("%v tickets for %v %v", userTickets, firstName, lastName)
  time.Sleep(10 * time.Second)
  fmt.Println("####################")
  fmt.Printf("Sending ticket:\n %v to email address %v\n", ticket, email)
  fmt.Println("####################")

  wg.Done()
}
