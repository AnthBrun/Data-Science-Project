tageswerte <- read.csv("C:\\Users\\Anthony\\OneDrive - FHDO - PROD\\Informatik\\3. Semester\\Programmierkurs II\\Data Science Projekt\\Data preprocessing\\tageswerte_KL_collected.csv")

tageswerte %<>% mutate_all(~replace(., . == -999, NA))

df_mean <- tageswerte %>%
  group_by(MESS_DATUM) %>%
  summarize(mean_TXK = mean(TXK, na.rm = TRUE),
            mean_TNK = mean(TNK, na.rm = TRUE))

df_filtered <- df_mean[complete.cases(df_mean), ]

df_filtered %<>%  mutate(Phänomen = case_when(
  df_filtered$mean_TXK >= 30 ~ "Heißtag",
  df_filtered$mean_TXK >= 25 & df_filtered$mean_TXK < 30 ~ "Sommertag",
  df_filtered$mean_TXK <= 0 ~ "Eistag",
  df_filtered$mean_TNK <= 0 & df_filtered$mean_TXK > 0 ~ "Frosttag",
  TRUE ~ NA_character_
))

df_filtered$Year <- lubridate::year(df_filtered$MESS_DATUM)

df_counts <- df_filtered %>%
  group_by(Year, Phänomen) %>%
  summarise(Count = n())

plot <- ggplot(df_counts, aes(x = Year, y = Count, fill = Phänomen)) +
  geom_bar(stat = "identity", position = "stack") +
  geom_smooth(method="loess", se=FALSE, color="black") +
  labs(title = "Jährliche Anzahl der Phänomene seit 1824 bis 2022", y = "Anzahl in Tagen", subtitle = "Errechnet aus den täglichen Durchschnittstemperaturen in Deutschland") +
  scale_fill_manual(values = c("Heißtag" = "red", "Sommertag" = "orange", "Frosttag" = "lightblue", "Eistag" = "blue")) +
  facet_wrap(~ Phänomen, scales = "free_y") +
  theme_minimal() +
  theme(legend.position = "bottom",
        legend.direction = "horizontal")

plot
ggsave("Anzahl Wetterphänomene.jpg")
