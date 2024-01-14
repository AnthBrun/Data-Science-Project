library("ggplot2")
library("tidyverse")

tageswerte_KL_collected <- read.csv("C:\\Users\\Anthony\\OneDrive - FHDO - PROD\\Informatik\\3. Semester\\Programmierkurs II\\Data Science Projekt\\Data preprocessing\\tageswerte_KL_collected.csv")

tageswerte_KL_collected$MESS_DATUM <- as.Date(tageswerte_KL_collected$MESS_DATUM, format = "%Y-%m-%d")

df <- tageswerte_KL_collected[, c("STATIONS_ID", "MESS_DATUM")]

df_count <- df %>%
  group_by(MESS_DATUM) %>%
  summarise(Station_Count = n_distinct(STATIONS_ID))

plot <- ggplot(df, aes(x = MESS_DATUM)) +
  geom_density() +
  labs(title = "Dichte an Messstationen", x = "Jahr", y = "Stations-ID") +
  theme_minimal() +
  scale_x_date(date_breaks = "50 years", date_labels = "%Y")

plot_station_count <- ggplot(df_count, aes(x = MESS_DATUM, y = Station_Count)) +
  geom_line(color = "blue") +
  labs(title = "Anzahl der Wetterstationen in Deutschland seit 1824", 
       x = "Jahr", 
       y = "Anzahl der Stationen",
       subtitle = "Anhand der Station-IDs ermittelt") +
  theme_minimal() +
  scale_x_date(date_breaks = "20 years", date_labels = "%Y") +
  xlim(as.Date("1824-01-01"), max(df_count$MESS_DATUM))

plot_station_count

plot
ggsave("Messstationen.jpg")
