--DEPT TABLE CONSTRAINTS
ALTER TABLE dept
ADD constraint pk_dept PRIMARY KEY (deptno);
ALTER TABLE dept
MODIFY (dname NOT NULL);
ALTER TABLE dept
MODIFY (loc NOT NULL);

--EMP TABLE CONSTRAINTS
ALTER TABLE emp
ADD constraint pk_emp PRIMARY KEY (empno);
ALTER TABLE emp
MODIFY (ename NOT NULL);
ALTER TABLE emp
MODIFY (job NOT NULL);
ALTER TABLE emp
MODIFY (hiredate NOT NULL);
ALTER TABLE emp
MODIFY (sal NOT NULL);
ALTER TABLE emp
ADD CONSTRAINT fk_emp_deptno FOREIGN KEY (deptno) REFERENCES DEPT(deptno);
----------------INSERT/ADD PROCEDURES----------------
--------------------------------------------------------------------------------------------------
create or replace PROCEDURE Add_emp(
      pemp_no NUMBER,
      pename VARCHAR2,
      pjob VARCHAR2,
      pmgr NUMBER,
      phiredate DATE,
      psal NUMBER,
      pcomm NUMBER,
      pdeptno NUMBER)
IS
    muy_grande EXCEPTION;
    PRAGMA EXCEPTION_INIT(muy_grande, -12899);
    no_numero EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_numero, -01722);
    no_permitido EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_permitido, -00984);
    dato_inconsistente EXCEPTION;
    PRAGMA EXCEPTION_INIT(dato_inconsistente, -00932);
    restriccion_unica EXCEPTION;
    PRAGMA EXCEPTION_INIT(restriccion_unica, -00001);
    not_null_constraint  EXCEPTION;
    PRAGMA EXCEPTION_INIT(not_null_constraint,-01400);
    no_existe_dept  EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_existe_dept,-02291);

BEGIN
    INSERT INTO emp
    VALUES(pemp_no, pename, pjob, pmgr, phiredate, psal, pcomm, pdeptno);
    COMMIT;
    EXCEPTION
        WHEN muy_grande THEN
            RAISE_APPLICATION_ERROR(-20000, 'ERROR: El valor de una columna es demasiado grande');
        WHEN no_numero THEN
            RAISE_APPLICATION_ERROR(-20001, 'ERROR: Tipo de dato numerico no valido');
        WHEN no_permitido THEN
            RAISE_APPLICATION_ERROR(-20002, 'ERROR: Columna no permitida');
        WHEN dato_inconsistente THEN
            RAISE_APPLICATION_ERROR(-20003, 'ERROR: Tipos de dato inconsistente');
        WHEN restriccion_unica THEN
            RAISE_APPLICATION_ERROR(-20004, 'ERROR: Restriccion unica violada');
        WHEN not_null_constraint THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Una columna no admite valores nulos');
        WHEN no_existe_dept THEN
            RAISE_APPLICATION_ERROR(-20017, 'ERROR: El departamento no existe');
END;
--------------------------------------------------------------------------------------------------
create or replace PROCEDURE Add_depto(
      pdepno NUMBER,
      pdname VARCHAR2,
      ploc VARCHAR2)
IS
    muy_grande EXCEPTION;
    PRAGMA EXCEPTION_INIT(muy_grande, -12899);
    no_numero EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_numero, -01722);
    no_permitido EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_permitido, -00984);
    dato_inconsistente EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_permitido, -00932);
    restriccion_unica EXCEPTION;
    PRAGMA EXCEPTION_INIT(restriccion_unica, -00001);
    not_null_constraint  EXCEPTION;
    PRAGMA EXCEPTION_INIT(not_null_constraint,-01400);

BEGIN
    INSERT INTO dept
    VALUES (pdepno, pdname, ploc);
    COMMIT;
    EXCEPTION
        WHEN muy_grande THEN
            RAISE_APPLICATION_ERROR(-20000, 'ERROR: El valor de una columna es demasiado grande');
        WHEN no_numero THEN
            RAISE_APPLICATION_ERROR(-20001, 'ERROR: Tipo de dato numerico no valido');
        WHEN no_permitido THEN
            RAISE_APPLICATION_ERROR(-20002, 'ERROR: Columna no permitida');
        WHEN dato_inconsistente THEN
            RAISE_APPLICATION_ERROR(-20003, 'ERROR: Tipos de dato inconsistente');
        WHEN restriccion_unica THEN
            RAISE_APPLICATION_ERROR(-20004, 'ERROR: Restriccion unica violada');
        WHEN not_null_constraint THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Una columna no admite valores nulos');

END;
--------------------------------------------------------------------------------------------------
----------------DELETE PROCEDURES----------------
create or replace PROCEDURE delete_depto(pdeptno NUMBER)
IS
    no_existe EXCEPTION;
    emp_en_dept EXCEPTION;
    PRAGMA EXCEPTION_INIT(emp_en_dept, -02292);
BEGIN
    DELETE FROM dept
    WHERE deptno = (SELECT deptno
                        FROM DEPT
                        WHERE deptno = pdeptno);
    IF SQL%ROWCOUNT = 0
    THEN
        RAISE no_existe;
    END IF;
    COMMIT;
EXCEPTION
    WHEN no_existe THEN
        RAISE_APPLICATION_ERROR(-20001, 'ERROR: No existe el departamento');
    WHEN emp_en_dept THEN
        RAISE_APPLICATION_ERROR(-20002, 'ERROR: El departamento tiene empleados');
END;
--------------------------------------------------------------------------------------------------
create or replace PROCEDURE delete_emp(pempno NUMBER)
IS
     no_existe EXCEPTION;
BEGIN
    DELETE FROM emp
    WHERE empno = (SELECT empno
                    FROM emp
                    WHERE empno = pempno);
    IF SQL%ROWCOUNT = 0
    THEN
        RAISE no_existe;
    END IF;
    COMMIT;
    EXCEPTION
        WHEN no_existe THEN
            RAISE_APPLICATION_ERROR(-20001, 'ERROR: No existe el empleado');
END;
--------------------------------------------------------------------------------------------------
----------------UPDATE PROCEDURES----------------
create or replace PROCEDURE Update_emp(
      pemp_no NUMBER,
      pename VARCHAR2,
      pjob VARCHAR2,
      pmgr NUMBER,
      phiredate DATE,
      psal NUMBER,
      pcomm NUMBER,
      pdeptno NUMBER)
IS
    actualizar_null EXCEPTION;
    PRAGMA EXCEPTION_INIT(actualizar_null, -01407);
    muy_grande EXCEPTION;
    PRAGMA EXCEPTION_INIT(muy_grande, -12899);
    no_numero EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_numero, -01722);
    no_permitido EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_permitido, -00984);
    dato_inconsistente EXCEPTION;
    PRAGMA EXCEPTION_INIT(dato_inconsistente, -00932);
    restriccion_unica EXCEPTION;
    PRAGMA EXCEPTION_INIT(restriccion_unica, -00001);
    not_null_constraint  EXCEPTION;
    PRAGMA EXCEPTION_INIT(not_null_constraint,-01400);
    no_existe_dept  EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_existe_dept,-02291);

BEGIN
    UPDATE emp
    SET ename = pename, job = pjob, mgr = pmgr,
    hiredate = phiredate, sal = psal, comm = pcomm, deptno = pdeptno
    WHERE  empno = pemp_no;
    COMMIT;
    EXCEPTION
        WHEN no_data_found THEN
            RAISE_APPLICATION_ERROR(-20011, 'ERROR: El empleado no existe');
        WHEN muy_grande THEN
            RAISE_APPLICATION_ERROR(-20012, 'ERROR: El valor de una columna es demasiado grande');
        WHEN no_numero THEN
            RAISE_APPLICATION_ERROR(-20013, 'ERROR: Tipo de dato numerico no valido');
        WHEN no_permitido THEN
            RAISE_APPLICATION_ERROR(-20014, 'ERROR: Columna no permitida');
        WHEN dato_inconsistente THEN
            RAISE_APPLICATION_ERROR(-20015, 'ERROR: Tipos de dato inconsistente');
        WHEN restriccion_unica THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Restriccion unica violada');
        WHEN not_null_constraint THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Una columna no admite valores nulos');
        WHEN no_existe_dept THEN
            RAISE_APPLICATION_ERROR(-20017, 'ERROR: El departamento no existe');
        WHEN actualizar_null THEN
            RAISE_APPLICATION_ERROR(-20018, 'ERROR: No se pueden actualizar valores a NULL');

END;
--------------------------------------------------------------------------------------------------
create or replace PROCEDURE update_depto(
    pdeptno NUMBER,
    pdname VARCHAR2,
    ploc VARCHAR2)
IS
    muy_grande EXCEPTION;
    PRAGMA EXCEPTION_INIT(muy_grande, -12899);
    no_numero EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_numero, -01722);
    no_permitido EXCEPTION;
    PRAGMA EXCEPTION_INIT(no_permitido, -00984);
    dato_inconsistente EXCEPTION;
    PRAGMA EXCEPTION_INIT(dato_inconsistente, -00932);
    restriccion_unica EXCEPTION;
    PRAGMA EXCEPTION_INIT(restriccion_unica, -00001);
    not_null_constraint  EXCEPTION;
    PRAGMA EXCEPTION_INIT(not_null_constraint,-01400);
    actualizar_null EXCEPTION;
    PRAGMA EXCEPTION_INIT(actualizar_null, -01407);
BEGIN
    UPDATE DEPT
    SET dname = pdname, loc = ploc
    WHERE deptno = pdeptno;
    COMMIT;
    EXCEPTION
        WHEN no_data_found THEN
            RAISE_APPLICATION_ERROR(-20011, 'ERROR: El departamento no existe');
        WHEN muy_grande THEN
            RAISE_APPLICATION_ERROR(-20012, 'ERROR: El valor de una columna es demasiado grande');
        WHEN no_numero THEN
            RAISE_APPLICATION_ERROR(-20013, 'ERROR: Tipo de dato numerico no valido');
        WHEN no_permitido THEN
            RAISE_APPLICATION_ERROR(-20014, 'ERROR: Columna no permitida');
        WHEN dato_inconsistente THEN
            RAISE_APPLICATION_ERROR(-20015, 'ERROR: Tipos de dato inconsistente');
        WHEN restriccion_unica THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Restriccion unica violada');
        WHEN not_null_constraint THEN
            RAISE_APPLICATION_ERROR(-20016, 'ERROR: Una columna no admite valores nulos');
        WHEN actualizar_null THEN
            RAISE_APPLICATION_ERROR(-20017, 'ERROR: No se pueden actualizar valores a NULL');

END;


----------------------------------------------------------------------------
---------------------------------------------------------

create or replace NONEDITIONABLE FUNCTION no_emp_deptno
(pdepno dept.deptno%TYPE) RETURN NUMBER
IS
    cant_employees NUMBER;
BEGIN
    SELECT COUNT(empno)
    INTO cant_employees
    FROM emp
    WHERE deptno = pdepno;
    IF cant_employees = 0 THEN
        RAISE no_data_found;
    END IF;
    RETURN cant_employees;

    EXCEPTION
        WHEN no_data_found THEN
            RETURN -1;
END no_emp_deptno;

