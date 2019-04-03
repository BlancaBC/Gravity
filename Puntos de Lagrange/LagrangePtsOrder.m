function [L]=LagrangePtsOrder(pts)
 pts=double([vpa(pts.x),vpa(pts.y),vpa(pts.z)]);
 f=find( imag(pts(:,1))>-1e-37 & imag(pts(:,1))<1e-37 & imag(pts(:,2))==0 & imag(pts(:,3))==0);
 pts=real(pts(f,:));
 
L(1,:)=pts(1,:); L(2,:)=pts(5,:); L(3,:)=pts(9,:);
L(4,:)=pts(4,:); L(5,:)=pts(3,:);
end