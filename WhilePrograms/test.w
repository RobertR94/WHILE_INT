define name DO
    LOOP x DO
        x_0 = x_0 + 1
    END
END
define name2 DO
    LOOP y DO
        y = y + 2
    END
    y = y + 3
END
WHILE x != 0 DO
    x := x - 1
END