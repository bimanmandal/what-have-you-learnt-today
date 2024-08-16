## Gorm and Swagger

### Gorm
I used a PostgreSQL database to read and explore data through the API. While the steps I followed weren't exactly ideal, I established a connection using a library from psql and then executed database queries to retrieve and examine the data.

The steps

1. Get the package

```bash
go get "github.com/lib/pq"
```

2. Create the connection

```go
psqlInfo := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",Host, Port, User, Password, Database)
db, err := sql.Open("postgres", psqlInfo)
```

3. Query the data

```go
p.DB.Query(sqlStatement)
```

I discovered that the same can be easily achieved using the GORM library in Go, making the process straightforward and simple.

1. Get the package

```bash
go get   "gorm.io/driver/postgres"
go get   "gorm.io/gorm"

```

2. Create the connection

```go
psqlInfo := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",Host, Port, User, Password, Database)
db, err := gorm.Open(postgres.Open(psqlInfo), &gorm.Config{})
```

3. Declare the model
```go
type Customer struct {
  Id           string `json:"id" gorm:"column:cid"`
  Name         string `json:"name" gorm:"column:cname"`
  Mobile       string `json:"mobile" gorm:"column:mno"`
  LastSeen     string `json:"lastSeen" gorm:"column:updated_on"`
}
```

4. Execute the query and have fun. In our case we have queried the customer by id
```go
var customer mo.Customer
p.DB.First(&Customer, "cid = ?", id)
```

More details about gorm can be found here https://gorm.io/docs/


### Swagger in GoFiber

Among the various Go APIs I've explored, including `gin`, `gorilla/mux`, and `gofiber`, I found that I prefer using `gofiber`.

While working with GoFiber, I wanted to add documentation for the APIs. I learned that generating Swagger documentation isn't as simple as just adding a library and using it. It involves several steps:
1. Install `swag`.
```bash
go install github.com/swaggo/swag/cmd/swag@latest
```
2. Add proper comments in the code.
  ```go
  // Customers godoc
  //
  //  @Summary      Get list of Customers
  //  @Description  Get Customers
  //  @Tags         customers
  //  @Accept       json
  //  @Produce      json
  //  @Success      200  {array}  mo.Customer
  //  @Router       /customers [get]
  func (d *CustomerHandler) ListCustomers(c *fiber.Ctx) error {
    return c.JSON(d.db.GetCustomers())
  }
  ```
   > You can refer to this https://github.com/swaggo/swag?tab=readme-ov-file and [example](https://github.com/swaggo/swag/tree/master/example/celler) for more details.
3. Generate the Swagger JSON using `swag`.
```bash
~/go/bin/swag init -g cmd/main.go
```
4. Create the necessary configurations.
```go
cfg := swagger.Config{
    BasePath: "/docs",
    Path:     "docs",
    FilePath: "./docs/swagger.json",
    Title:    "Swagger API Docs",
  }
```
5. Install and Import swagger contri
```bash
go get "github.com/gofiber/contrib/swagger"
```
```go
import "github.com/gofiber/contrib/swagger"
```
6. Add the required middleware.
```go
app.Use(swagger.New(cfg))
```


If you want to include ReDoc along with Swagger, I highly recommend ReDoc for its clear and easy-to-read presentation of Swagger documentation. To integrate ReDoc, you’ll need the Swagger JSON and then follow these steps:
1. Add the ReDoc package.
```bash
go get "github.com/mvrilo/go-redoc"
```
2. Create the configurations.
```go
doc := redoc.Redoc{
    Title:       "Customer Status API",
    Description: "Customer Status",
    SpecFile:    "./docs/swagger.json",
    SpecPath:    "/swagger.json",
    DocsPath:    "/redoc",
  }
```
3. Incorporate it into the middleware.
```go
app.Use(fiberredoc.New(doc))
```

Now you can visit your http://server/swagger.json for the swagger files
and http://server/redoc for the redoc docs
