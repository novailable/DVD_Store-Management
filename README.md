# DVD_Store-Management
## Introduction

The DVD store application is presented from the owner's perspective, where customers are required to create an account to rent items. The system enables the owner to manage the addition of movies, DVDs, customers, and DVD rentals and returns.
The primary objective of the system is to provide efficient access and seamless utilization of the large collection of movies, customer data, and associated information. This is accomplished by taking advantages of advanced data structures, such as Binary Search Trees and Linked Lists, which facilitate fast and effective search and retrieval of information, even when dealing with large amounts of data.
Overall, the DVD store application is designed to meet the needs of both the owner and the customers, providing a streamlined and effective way to manage and rent a vast collection of movies. By leveraging advanced data structures and optimization techniques, the system can operate at peak efficiency, allowing users to access the information they need quickly and easily.

## UML Class diagram

<img width="700" alt="image" src="https://github.com/novailable/DVD_Store-Management/assets/97833342/b8a7f27c-e50c-4e83-9856-d8dec829c067">

The software architecture shown in above is a representation of a system designed to manage a collection of movies and their associated DVD copies, as well as customer data. The system is divided into three base classes: Customer, Movie, and DVD, each with its own set of attributes and methods.
Customer class and binary tree will be merged inside ‘CustomerManager’ while movie, DVDs and linked list is merged at ‘DVDManager’. Then both managers’ classes are combined and connected with the main file throughout ‘Manager’

## Selection of Algorithms & Integration

The Customer class is responsible for storing customer data such as first name, last name, id, and account number. To efficiently manage a collection of customers, the system uses a Binary Search Tree (BST) data structure. This data structure is created in the Customer Manager class and is stored as '_customers'. Each node in this BST contains a 'Customer' object.
The Movie class, on the other hand, is responsible for storing movie details such as name, genre, directors, movie stars, etc. The DVD class is a subclass of the Movie class, and it stores information on the number of copies of a particular movie in the system, as well as the account numbers of customers who are currently renting each DVD. This relationship between the DVD and the Movie class is represented through a foreign key.
To efficiently manage a collection of DVDs and movies, the system uses two linked lists: '_dvd_l_list' and '_movie_l_list', respectively. These linked lists are each represented as a node in the DVDManager class. The DVDManager class is responsible for adding, removing, and updating DVD and movie information in the system.
To manage the entire system, the Manager class is used. This class imports the CustomerManager and DVDManager classes and connects the various components of the system. The Manager class is responsible for interacting with the system from the main.py file, allowing users to perform actions such as adding new customers, adding new movies, DVDs, renting DVDs, and returning DVDs.
