-- [II] SELECT 문 - 조회 /* 여러줄 주석 */
-- 1. SELECT 문 작성법
SHOW USER;
   -- 현재 계정(실행 : CTRL+ENTER)
SELECT * FROM TAB; -- 현 계정이 가지고 있는 테이블들
SELECT * FROM EMP; -- EMP테이블의 모든 열, 모든행
SELECT * FROM DEPT; -- DEPT테이블의 모든 열, 모든행
SELECT * FROM SALGRADE;

-- 2. 특정열만 출력
DESC EMP;
    -- EMP 테이블 구조를 나타내는 ORACLE 명령
SELECT EMPNO, ENAME, SAL, JOB FROM EMP; -- EMPNO, ENAME, SAL, JOB열만 모든 행 검색
SELECT EMPNO AS "사 번", ENAME AS "이름", SAL AS "급여", JOB FROM EMP;
SELECT EMPNO "사 번", ENAME "이름", SAL "급여", JOB FROM EMP;
SELECT EMPNO "사 번", ENAME 이름, SAL 급여, JOB FROM EMP;
SELECT EMPNO NO, ENAME ENAME, SAL SALARY FROM EMP;

-- 3. 특정 행 출력 : WHERE절(조건절) - 비교연산자 : 같다(=), 다르다(!=, ^=, <>), >, >=, <, <=
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL=3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL^=3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL<>3000;
SELECT EMPNO NO, ENAME, SAL FROM EMP WHERE SAL!=3000;
    -- 비교연산자는 숫자, 문자, 날짜형 모두 가능
    -- EX1) 사원이름(ENAME)이 'A','B','C'로 시작하는 사원의 모든 필드(열)
    -- 'A' < 'AA' < 'AAA' < 'AAAA' < 'B' < 'C' < 'D'
    SELECT * FROM EMP WHERE ENAME < 'D';
    --  EX2) 82년도 이전에 입사한 사원의 모든 필드
    SELECT * FROM EMP WHERE HIREDATE < '82/01/01';
    -- EX3) 부서번호(DEPTNO)가 10번인 사원의 모든 필드
    SELECT * FROM EMP WHERE DEPTNO=10;
    -- EX4) 이름(ENAME)이 FORD인 직원의 EMPNO, ENAME, MGR(상사의 사번)을 출력
    SELECT EMPNO, ENAME, MGR
        FROM EMP
        WHERE ENAME='FORD';
    -- SQL문은 대소문자 구별없음. 데이터 대소문자 구별
    select empno, ename, mgr from emp where ename='FORD';
    
-- 4. 특정 행 출력 : WHERE절(조건절) - 논리연산자 : AND, OR, NOT
    -- EX1. 급여(SAL)가 2000이상 3000이하인 직원의 모든 필드
    SELECT * FROM EMP WHERE 2000<=SAL AND SAL<=3000;
    -- EX2. 82년도에 입사한 사원의 모든 필드
    SELECT * FROM EMP WHERE HIREDATE >= '82/01/01' AND HIREDATE<='82/12/31';
    
    -- 날짜 표기법 세팅(현재 : YY/MM/DD 또는  RR/MM/DD)
    ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
    ALTER SESSION SET NLS_DATE_FORMAT = 'RR/MM/DD';
    SELECT * FROM EMP;
    SELECT TO_CHAR(HIREDATE, 'YY/MM/DD') FROM EMP;
    -- 날짜 셋팅을 고려한 82년도 입사한 사원의 모든 필드
    SELECT * FROM EMP 
        WHERE TO_CHAR(HIREDATE, 'YY/MM/DD') >= '82/01/01' AND 
            TO_CHAR(HIREDATE, 'YY/MM/DD')<='82/12/31';
    -- EX3. 연봉이 2400이상인 직원의 ENAME, SAL, 연봉(SAL*12)을 출력
    SELECT ENAME, SAL, SAL*12 ANNUALSAL -- (3)
        FROM EMP            -- (1)
        WHERE SAL*12>=2400;  -- (2) WHERE절에는 필드의 별칭 사용 불가
    -- EX4. 연봉이 3000이상인 직원의 ENAME, SAL, 연봉을 연봉순으로 출력
    SELECT ENAME, SAL, SAL*12 연봉 -- (3)
        FROM EMP              -- (1) 
        WHERE SAL*12>=3000    -- (2)WHERE절에는 필드의 별칭 사용 불가
        ORDER BY 연봉;   -- (4) ORDER BY절에는 필드의 별칭 사용 가능
    -- EX5 JOB이 MANAGER이거나 10번 부서(DEPTNO) 외의 직원 모든 필드
    SELECT * FROM EMP WHERE JOB='MANAGER' OR DEPTNO!=10;
        
-- 5. 산술연산자(SELECT절, 조건절, ORDER BY절) 
    -- 모든 사원의 10% 인상된 월급과 사번(EMPNO), 이름(ENAME)을 출력
    SELECT EMPNO, ENAME, SAL*1.1 FROM EMP;
    -- 모든 사원의 이름(ENAME), 월급(SAL), 상여(COMM), 연봉(SAL*12+COMM)을 출력
    SELECT ENAME, SAL, COMM, SAL*12+COMM 연봉 FROM EMP;
    -- 산술연산의 결과는 NULL을 포함하면 결과도 NULL
    -- NVL(NULL일 수도 있는 필드명, NULL을 대체할 값)을 이용
    SELECT ENAME, SAL, COMM, NVL(COMM, 0), SAL*12+NVL(COMM, 0) 연봉 FROM EMP;
    -- 모든사원의 사번, 이름, 상사사번(상사가 없으면 'CEO'로 출력) 출력
    SELECT * FROM EMP;
    
    -- 6. 연결연산자 : 필드값이나 문자르 연결
    SELECT ENAME || '은' || HOB EMPLOYEE FROM EMP;
    
    -- 7. 중복제거
    SELECT DISTINCT JOB FROM EMP;
    SELECT DISTINCT DEPTNO FROM EMP;
    
    -- 연습문제
    <총 연습문제>
--1.	EMP 테이블에서 sal이 3000이상인 사원의 empno, ename, job, sal을 출력
      SELECT EMPNO, ENAME, JOB, SAL*12
      FROM EMP
      WHERE SAL*12>=3000;
      
--2.	EMP 테이블에서 empno가 7788인 사원의 ename과 deptno를 출력
      SELECT ENAME, DEPTNO
      FROM EMP
      WHERE EMPNO=7788;
--3.	연봉(SAL*12+COMM)이 24000이상인 사번, 이름, 급여 출력 (급여순정렬)
    SELECT EMPNO, ENAME, (SAL*12 + NVL(COMM, 0))  연봉
    FROM EMP
    WHERE (SAL*12 + NVL(COMM, 0)) >= 24000
    ORDER BY 연봉;

--4.	입사일이 1981년 2월 20과 1981년 5월 1일 사이에 입사한 사원의 사원명, 직책, 입사일을 출력 (단 hiredate 순으로 출력)

    SELECT ENAME, HIREDATE
    FROM EMP WHERE HIREDATE >= '81/02/20' AND HIREDATE<='81/05/01'
    ORDER BY HIREDATE;
--5.	deptno가 10,20인 사원의 모든 정보를 출력 (단 ename순으로 정렬)
    SELECT * FROM EMP WHERE DEPTNO IN (10, 20)
    ORDER BY ENAME;
--6.	sal이 1500이상이고 deptno가 10,30인 사원의 ename과 sal를 출력
-- (단 출력되는 결과의 타이틀을 employee과 Monthly Salary로 출력)
    SELECT ENAME AS EMPLOYEE, SAL AS SALARY
    FROM EMP WHERE SAL >=1500 AND DEPTNO IN(10, 30);
--7.	hiredate가 1982년인 사원의 모든 정보를 출력
     SELECT * FROM EMP WHERE HIREDATE >= '82/01/01' AND HIREDATE<='82/12/31'
--8.	이름의 첫자가 C부터  P로 시작하는 사람의 이름, 급여 이름순 정렬
SELECT ENAME, SAL
FROM EMP 
WHERE ENAME >= 'C' AND ENAME < 'Q'
ORDER BY ENAME;


--9.	comm이 sal보다 10%가 많은 모든 사원에 대하여 이름, 급여, 상여금을 
--출력하는 SELECT 문을 작성
     SELECT ENAME, SAL, COMM
     FROM EMP
     WHERE COMM >= SAL*1.1;
--10.	job이 CLERK이거나 ANALYST이고 sal이 1000,3000,5000이 아닌 모든 사원의 정보를 출력
    SELECT *
    FROM EMP
    WHERE (JOB = 'CLERK' OR JOB = 'ANALYST')
      AND SAL NOT IN (1000, 3000, 5000);

--11.	ename에 L이 두 자가 있고 deptno가 30이거나 또는 mgr이 7782인 사원의 
--모든 정보를 출력하는 SELECT 문을 작성하여라.
    SELECT *
    FROM EMP
    WHERE (LENGTH(REPLACE(ENAME, 'L', '')) <= LENGTH(ENAME) - 2)
      AND (DEPTNO = 30 OR MGR = 7782);

--12.	입사일이 81년도인 직원의 사번, 사원명, 입사일, 업무, 급여를 출력
    SELECT * FROM EMP
    WHERE HIREDATE >= '81/01/01' AND HIREDATE<='82/01/01';
--13.	입사일이81년이고 업무가 'SALESMAN'이 아닌 직원의 사번, 사원명, 입사일, 
-- 업무, 급여를 검색하시오.
SELECT * FROM EMP
    WHERE HIREDATE >= '81/01/01' AND HIREDATE<='82/01/01';



    
    