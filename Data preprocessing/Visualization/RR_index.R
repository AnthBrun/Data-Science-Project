RRindex <- monatswerte_RRINDEX_collected

RRindex %<>% mutate_all(~replace(., . == -999, NA)) 

generalRR_mean <- RRindex %>% group_by(MESS_DATUM_BEGINN) %>%
  summarize(mean_RR_0_1 = mean(MO_RR_GE_0_1_MM, na.rm = TRUE))

extremeRR_mean <- RRindex %>% group_by(MESS_DATUM_BEGINN) %>% 
  summarize(mean_RR_20 = mean(MO_RR_GE_20_0_MM, na.rm = TRUE))

generalRR_mean_filtered <- generalRR_mean[complete.cases(generalRR_mean), ]

generalRR_mean_filtered$MESS_DATUM_BEGINN <- 
  as.Date(generalRR_mean_filtered$MESS_DATUM_BEGINN) 

extremeRR_mean_filtered <- extremeRR_mean[complete.cases(extremeRR_mean), ]

extremeRR_mean_filtered$MESS_DATUM_BEGINN <- 
  as.Date(extremeRR_mean_filtered$MESS_DATUM_BEGINN) 

generalRR_plot <- ggplot(generalRR_mean_filtered, aes(x = MESS_DATUM_BEGINN, 
                                                      y = mean_RR_0_1)) +
  geom_line(color = "blue") +
  labs(title = "Monatliche Anzahl an Tagen mit einer Niederschlagshöhe >= 0.1mm",
       y = "Anzahl an Tagen", x = "Zeitraum") +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  theme_minimal() +
  theme(axis.line.x = element_blank(),
        axis.ticks.x = element_blank(),
        axis.title.x = element_blank(),
        legend.title = element_blank(),
        legend.position = "bottom")

generalRR_plot
ggsave("Niederschlagshöhe_mittel_0_1_mm.jpg")

extremeRR_plot <- ggplot(extremeRR_mean_filtered, aes(x = MESS_DATUM_BEGINN, 
                                                      y = mean_RR_20)) +
  geom_line(color = "blue") +
  labs(title = "Monatliche Anzahl an Tagen mit einer Niederschlagshöhe >= 20mm",
       y = "Anzahl an Tagen", x = "Zeitraum") +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  theme_minimal() +
  theme(axis.line.x = element_blank(),
        axis.ticks.x = element_blank(),
        axis.title.x = element_blank(),
        legend.title = element_blank(),
        legend.position = "bottom")

extremeRR_plot
ggsave("Niederschlagshöhe_mittel_20_mm.jpg")


snow <- RRindex %>% group_by(MESS_DATUM_BEGINN) %>%
  summarize(mean_SH_1 = mean(MO_SH_GE_1_0_CM, na.rm = TRUE))

snow_mean <- snow[complete.cases(generalRR_mean), ]
snow_mean$MESS_DATUM_BEGINN <- 
  as.Date(snow_mean$MESS_DATUM_BEGINN) 

snow_mean_plot <- ggplot(snow_mean, aes(x = MESS_DATUM_BEGINN, 
                                                      y = mean_SH_1)) +
  geom_line(color = "blue") +
  labs(title = "Monatliche Anzahl an Tagen mit einer Schneehöhe >= 1cm",
       y = "Anzahl an Tagen", x = "Zeitraum") +
  theme_minimal() +
  geom_smooth(method = "loess", se=FALSE, color = "red") +
  theme(axis.line.x = element_blank(),
        axis.ticks.x = element_blank(),
        axis.title.x = element_blank(),
        legend.title = element_blank(),
        legend.position = "bottom")

snow_mean_plot
ggsave("Schneehoehe_mittel_1_cm.jpg")
