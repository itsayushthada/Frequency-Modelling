base_loc <- "D:\\Ayush\\Mech-Project\\Vibration-Analysis\\Data\\"

train_data <- paste0(base_loc, "Fixed-Fixed.csv")
test_data <- paste0(base_loc, "Fixed-Fixed-Test.csv")

df1 <- read.csv(train_data)
df2 <- read.csv(test_data)

library("ggplot2")

idx <- df1$Mode == 1

ggplot(data = df1[idx, ], aes(x="l1", y="l2", z="Frequency")) + geom_curve()